#/usr/local/bin/ python3
import numpy as np 
import matplotlib.pyplot as plt 
import open3d as o3d

if __name__ == '__main__':
    
    # create a variable for storing the pcd
    pcd_o3d = o3d.geometry.PointCloud()
    
    pcd_o3d = o3d.io.read_point_cloud("data/bunny.ply")
    
    o3d.visualization.draw_geometries([pcd_o3d])
    

    
    
    #How to display using matplotlib
    # create figure 
    # Convert the open3d object to numpy:
    pcd_np = np.asarray(pcd_o3d.points)
    fig , ax =plt.subplots(subplot_kw={"projection": "3d"})
    
    ax.scatter3D(pcd_np[:,0], pcd_np[:,1], pcd_np[:,2])
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    
    ax.set_title("Pointcloud using open3d in matplotlib")
    
    plt.show()

    
