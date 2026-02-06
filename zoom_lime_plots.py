#!/usr/bin/env python3
"""
Zoom in on LIME plots by cropping whitespace and scaling up
"""

from PIL import Image, ImageOps
import numpy as np
import os

def auto_crop_and_zoom(img_path, output_path, margin=20, zoom_factor=1.3):
    """
    Auto-crop whitespace and zoom in on the main content
    """
    # Open image
    img = Image.open(img_path)
    
    # Convert to numpy array
    img_array = np.array(img)
    
    # Find non-white pixels
    # Consider pixels with any channel < 250 as content
    if len(img_array.shape) == 3:
        content_mask = np.any(img_array < 250, axis=2)
    else:
        content_mask = img_array < 250
    
    # Find bounding box of content
    rows = np.any(content_mask, axis=1)
    cols = np.any(content_mask, axis=0)
    
    if rows.any() and cols.any():
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        
        # Add margin
        height, width = img_array.shape[:2]
        rmin = max(0, rmin - margin)
        rmax = min(height, rmax + margin)
        cmin = max(0, cmin - margin)
        cmax = min(width, cmax + margin)
        
        # Crop
        cropped = img.crop((cmin, rmin, cmax, rmax))
    else:
        cropped = img
    
    # Zoom in by scaling up
    width, height = cropped.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
    
    zoomed = cropped.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Save
    zoomed.save(output_path, 'PNG', quality=95, optimize=True)
    
    crop_info = f"Cropped from {img.size} to {cropped.size}, then zoomed to {zoomed.size}"
    return crop_info

def main():
    """
    Main function to zoom in on all LIME plots
    """
    media_dir = '/home/kangah/Desktop/MasterThesisLsu/media'
    
    # List of LIME plots to zoom
    lime_plots = [
        'lime_et.png',
        'lime_rf.png',
        'lime_examples.png'
    ]
    
    print("Zooming in on LIME plots...\n")
    
    for plot_name in lime_plots:
        input_path = os.path.join(media_dir, plot_name)
        
        if os.path.exists(input_path):
            # Zoom and crop directly
            # Create temporary backup with PNG extension
            temp_backup = input_path.replace('.png', '_temp.png')
            img = Image.open(input_path)
            img.save(temp_backup, 'PNG')
            
            # Zoom and crop
            crop_info = auto_crop_and_zoom(temp_backup, input_path, margin=30, zoom_factor=1.3)
            
            # Remove temp backup
            os.remove(temp_backup)
            
            print(f"✓ Zoomed: {plot_name}")
            print(f"  {crop_info}\n")
        else:
            print(f"✗ Not found: {plot_name}\n")
    
    print("✓ All LIME plots zoomed successfully!")
    print("\nThe plots are now:")
    print("  • Cropped to remove excess whitespace")
    print("  • Zoomed in by 30% for better detail")
    print("  • Even more readable for thesis printing")

if __name__ == "__main__":
    main()
