# Medical Image Segmentation - Brain grey matter segmentation

Small tool made with SimpleITK to segment parts or abnormalities on an organ based on MRI scans.

This tool is speicialized to segment and create a segmentation mask for the grey matter of the human brain.

However the same can be used to segment any other MRI scans.

The tool requires five inputs,

*   The input 2D image of the brain, a MRI scan image. The image can be from any anatomical plane.
    An example image from the transverse plane, brain.mha is included along with the repository.

*   Output image name.

*   Minimum grey scale color pixel value ranging between 0-255.

*   Maximum grey scale color pixel value ranging between 0-255. 
    *NOTE: Grey matter is usually higher than 90 on a perfect MRI.

*   The X co-ordinate of the grey matter from the grey matter column at the centre of the image.
*   The Y co-ordinate of the grey matter from the grey matter column at the centre of the image.
    *The point created from this X,Y co-ordinate is used as the reference seed point from which the segmentation starts. 
    *NOTE: You can use the [SNAP-ITK](http://www.itksnap.org/pmwiki/pmwiki.php) software to find the X,Y co-ordinate.

Examples cmd to run the tool:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**python createSegmentationMask.py brain.mha greyMatter.mha 90 256 192 162**

Example input image included with repository -> brain.mha
Example output segmentation mask included with repository -> greyMatter.mha

**Requirements:**\
*   [pip install simpleitk](https://pypi.org/project/SimpleITK/)
