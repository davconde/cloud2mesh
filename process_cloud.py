import os

import numpy as np
import pymeshlab

import options


def cloud_processing(ms):
    '''
    Simplify cloud and compute normals
    '''
    # Point cloud simplification
    if options.simplif_prcnt < 100:
        print('Simplifying point cloud')
        m = ms.current_mesh()
        num_points = m.vertex_number()
        ms.point_cloud_simplification(
            samplenum=num_points*options.simplif_prcnt//100,
            bestsampleflag=True)

    # Compute normals
    print('Computing normals')
    ms.compute_normal_for_point_clouds(k=50, smoothiter=8,
                                       flipflag=False, viewpos=[0, 0, 0])

    # Correct inverted normals
    m = ms.current_mesh()
    n_matrix = m.vertex_normal_matrix()
    plane_normals = n_matrix[np.abs(n_matrix[:, 2]) > 0.9, 2]
    if np.mean(plane_normals) < 0:
        ms.compute_normal_by_function_per_vertex(x='-nx', y='-ny', z='-nz')

    return ms


def surface_reconstruction(ms, cloud_name, pc_id):
    '''
    Reconstruct a texturized surface
    '''
    # Surface reconstruction
    print('Reconstructing surface')
    ms.generate_surface_reconstruction_screened_poisson(
        depth=8, samplespernode=1.5, pointweight=4.0)

    # Clean mesh from large faces from bad triangulation
    # and noise faces
    print('Cleaning mesh')
    ms.compute_selection_by_edge_length()
    ms.meshing_remove_selected_faces()
    ms.meshing_remove_connected_component_by_face_number()
    ms.meshing_remove_connected_component_by_diameter()
    ms.compute_selection_by_non_manifold_per_vertex()
    ms.meshing_remove_selected_faces()

    # Saving and texturizing the mesh
    print('Texturizing mesh')
    ms.compute_texcoord_by_function_per_vertex()
    ms.compute_texcoord_transfer_vertex_to_wedge()
    ms.compute_texcoord_parametrization_triangle_trivial_per_wedge(
        sidedim=0,
        textdim=options.textdim,
        border=4,
        method='Basic')
    ms.transfer_attributes_to_texture_per_vertex(
        sourcemesh=pc_id,
        targetmesh=ms.current_mesh_id(),
        textname=cloud_name + '_tex.png',
        textw=options.textdim,
        texth=options.textdim
    )

    return ms


def process_cloud(cloud_name):
    filename = os.getcwd() + '\\' + cloud_name
    mesh_path, ext = filename.rsplit('.', 1)
    name = mesh_path.rsplit('\\', 1)[-1]
    if not os.path.exists(mesh_path):
        os.makedirs(mesh_path)

    ms = pymeshlab.MeshSet()

    # Read point cloud
    print('Loading point cloud')
    ms.load_new_mesh(filename,
                     strformat=options.data_format,
                     separator='SPACE',
                     rgbmode=options.rgbmode)
    pc_id = ms.current_mesh_id()

    # Processing chain
    ms = cloud_processing(ms)
    ms = surface_reconstruction(ms, name, pc_id)

    # Save results
    ms.save_project(mesh_path + '\\' + name + '.mlp')
    ms.save_current_mesh(mesh_path + '\\' + name + '.obj',
                         save_wedge_texcoord=True)

    print('Processing finished')
