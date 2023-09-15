#/usr/local/bin/ python3
import numpy as np 
import matplotlib.pyplot as plt 
import open3d as o3d

if __name__ == '__main__':
    
    # create a numpy array for holding the pointcloud 
    number_points = 2000
    pcd_np = np.random.rand(number_points,3)
    
    # Convert to open3d format 
    pcd_o3d = o3d.geometry.PointCloud()
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd_np)
    
    #visualize the random numpy to pcd
    o3d.visualization.draw_geometries([pcd_o3d])