# perimetrics: measuring geometry of connected components
The following is an outline of the algorithm:
1. Read a grayscale image (as a 2D array) and the threshold at which the image is to be contoured
2. Contour the image vertex-by-vertex and distribute the area, perimeter values found at that vertex to the above-threshold cells surrounding that vertex, in a single pass through the image
3. Perform connected-component labeling to assign a unique integer (1 to N) to the cells of each connected component
4. In another single pass through the image, sum the area, perimeter values of the cells of the m-th connected component into the (m+1)-th element of a list, for 1 <= m <= N
5. Return the list containing area and perimeter values for each connected component

For connected-component labeling, the package <tt>connected-components-3d</tt> is used.
For contouring, the algorithm used is marching squares with linear interpolation of values between cell centers, based on:
*Utilizing Minkowski functionals for image analysis: a marching square algorithm*, Hubert Mantz *et al J. Stat. Mech.* (2008) P12015, DOI: 10.1088/1742-5468/2008/12/P12015

<p align="middle">
  <img src="/code_description_1.PNG" width="45%" />
  <img src="/code_description_2.PNG" width="45%" />
</p>
<p align="center">
**Figure 1.** Schematic diagrams illustrating the working of our code,
for two different kinds of vertices. In both cases, threshold value
equals 1. Left: one of the 4 cells around the vertex is above the
threshold, three are below. In this case the contour length (thin
red line) and area segment (shaded in pink) are both assigned to
that one cell. Right: Three of the cells are above the threshold and
one is below. In this case the contour length is divided equally
among the two cells bordering the below-threshold cell, and we
choose to divide up the enclosed area (pink) according to the thick
red lines shown here. (The exact method of dividing the values is
irrelevant for 8-connectivity.)
</p>


My main motivation for writing this code was that existing codes for computing Minkowski functionals usually give the *total* area above the threshold and the *total* length of the contour at that threshold. This obscures the study of geometry of the individual structures, and their statistics. For such studies using the total area and perimeter would mean contouring and measuring each connected component separately, which in turn would mean looping over the image N times, once for each connected component. For large random fields, if N scales linearly with the number of pixels N<sub>pix</sub>, then this approach would lead to a time complexity of *O*(N<sub>pix</sub> <sup>2</sup>). The approach used here has a time complexity of *O*(N<sub>pix</sub>), since it only needs two passes through the image.

