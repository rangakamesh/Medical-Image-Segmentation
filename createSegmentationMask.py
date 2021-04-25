import SimpleITK as sitk
import sys

#Reading the inputs
if len(sys.argv) != 7:
    print('Usage: ' + sys.argv[0] + ' <InputFilname> <OutputFilename> <Lower> <Upper> <SeedXCordinate> <SeedYCordinate>')
    sys.exit(1)
    
inputFilename = sys.argv[1]
outputFilename = sys.argv[2]
lower = float(sys.argv[3])
upper = float(sys.argv[4])

XCor = int(sys.argv[5])
YCor = int(sys.argv[6])

image = sitk.ReadImage(inputFilename, sitk.sitkFloat32)


#declare the image smoothing object
smoothing = sitk.CurvatureAnisotropicDiffusionImageFilter()

#set fine tuning parameters
smoothing.SetTimeStep(0.0125)
smoothing.SetNumberOfIterations(5)
smoothing.SetConductanceParameter(10.0)

#execute the image smoothing
smoothingOutput = smoothing.Execute(image)

#declare the image segmentation object
segmentation = sitk.IsolatedConnectedImageFilter()

#set segmentation fine tuning parameters
segmentation.SetLower(lower)
segmentation.SetUpper(upper)
# segmentation.SetSeed1([192,162])
segmentation.SetSeed1([XCor,YCor])
segmentation.SetReplaceValue(255)

#execute the segmentation
segmentationOutput = segmentation.Execute(smoothingOutput)

#write out the segmentation mask
sitk.WriteImage(segmentationOutput,outputFilename)

