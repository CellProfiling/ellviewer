Ellviewer
=========

Ellviewer (Emma Lundberg's lab viewer) is a simple online viewer to easily share your layered images. You just drop your files in any online accessible location and the static HTML viewer will take care of the rest.


Key features
------------

- Serverless Static HMTL viewer that you don't even need to host. That allows you to put a viewer anywhere you can place a URL.
- Zero code configuration. The behavior of the viewer is controlled by a simple CSV file. 
- Uses regular JPG/PNG files or direct image links.
- Adds transparency, coloring and transparency clipping on demand.
- Can display large images using a pyramidal file structure.


How to use it
-------------

Ellviewer works with the following file structure accesible online:
- A CSV file containing the metadata to be loaded/configured in the viewer
- [Optional] The images to be shown. If you use external URLs in the CSV metadata file, you don't need to host the images locally.
- [Optional] The `ellviewer.html` itself. Or you can use our hosted one here: https://lundberglab.stanford.edu/ellviewer/ellviewer.html

Let's check 3 examples of how to do it. You can find extensive information about all possible parameters in the later section.

**Example 1: basic external**:

- Populate and put this `metadata.csv` (you can find the file in the `examples/demo1` repository folder) file accessible online ( for demo purposes, this file is currently hosted in https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo1/metadata.csv ):

```
uri,name,clip,transparency,color,default
https://images.proteinatlas.org/41082/721_D4_1_red.jpg,microtubuli,,1.0,no,yes
https://images.proteinatlas.org/41082/721_D4_1_yellow.jpg,er,,1.0,no,yes
https://images.proteinatlas.org/41082/721_D4_1_blue.jpg,nuclei,,1.0,no,yes
https://images.proteinatlas.org/41082/721_D4_1_green.jpg,protein,,1.0,no,yes
```

- As you can see, the images are plain URLs containing regular jpg files. You can call the viewer just with the following URL: `https://lundberglab.stanford.edu/ellviewer/ellviewer.html?csv=[URL to your accessible metadata.csv]` ( for demo purposes, just try https://lundberglab.stanford.edu/ellviewer/ellviewer.html?csv=https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo1/metadata.csv )

**Example 2: totally hosted**:

- Choose a location accessible online and create `images` and `metadata` folders ( for demo purposes, this location is currently hosted in https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo2 )
- Populate and put this `metadata.csv` (you can find the file in the `examples/demo2` repository folder) file in the `metadata` folder created above ( for demo purposes, this file is currently hosted in https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo2/metadata/metadata.csv ):

```
uri,name,clip,transparency,color,default
HPA001223.jpg,HPA001223,,no,no,yes
segmentation.png,segmentation,,1.0,no,no
protein_bin.png,expression,,1.0,no,no
```

- Copy the images (you can find the images in the `examples/demo2/images` repository folder) to be shown inside the `images` folder ( for demo purposes, this location is currently hosted in https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo2/images/ )
- Copy the `ellviewer.html` file in the base level of the location ( for demo purposes, this location is currently hosted in https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo2 )

You can call the viewer just with the following URL: `[URL to your accessible location]/ellviewer.html` ( for demo purposes, just try https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo2/ellviewer.html )

**Example 3: big images**:

- Populate and put this `metadata.csv` (you can find the file in the `examples/demo3` repository folder) file accessible online ( for demo purposes, this file is currently hosted in https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo3/metadata.csv ):

```
uri,name,clip,transparency,color,default
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_AQP2.jpg,AQP2,,1.0,#0000ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_aSMA.jpg,aSMA,,1.0,#E40084,yes
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_ATM.jpg,ATM,,1.0,#ffff99,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_BCL2.jpg,BCL2,,1.0,#8000ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CAIX.jpg,CAIX,,1.0,#cc9900,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CAV.jpg,CAV,,1.0,#00ff80,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD1a.jpg,CD1a,,1.0,#0080ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD4.jpg,CD4,,1.0,#ffff00,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD8.jpg,CD8,,1.0,#959A3C,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD10.jpg,CD10,,1.0,#40ff40,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_Cd11c.jpg,Cd11c,,1.0,#4040ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD14.jpg,CD14,,1.0,#ff4040,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD31.jpg,CD31,,1.0,#FFA76B,yes
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD34.jpg,CD34,,1.0,#ff8040,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD45.jpg,CD45,,1.0,#40ff80,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD93.jpg,CD93,,1.0,#4080ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CD138.jpg,CD138,,1.0,#E9A3FF,yes
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CDH1.jpg,CDH1,,1.0,#808000,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CDK1.jpg,CDK1,,1.0,#ffff32,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_COLIV.jpg,COLIV,,1.0,#ff6600,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_CTNNB1.jpg,CTNNB1,,1.0,#ff8080,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_DAPI.jpg,DAPI,,1.0,#1EB4FF,yes
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_GATA3.jpg,GATA3,,1.0,#ff00c0,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_HIF1a.jpg,HIF1a,,1.0,#00c0ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_HIF2a.jpg,HIF2a,,1.0,#c0ff00,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_IFNA6.jpg,IFNA6,,1.0,#33cccc,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_IL6.jpg,IL6,,1.0,#ff4000,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_Ki67.jpg,Ki67,,1.0,#4000ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_NES.jpg,NES,,1.0,#0040ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_NF2.jpg,NF2,,1.0,#40ffff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_PanCK.jpg,PanCK,,1.0,#01786D,yes
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_PARP1.jpg,PARP1,,1.0,#ff40ff,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_PAX2.jpg,PAX2,,1.0,#c0c000,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_PCNA.jpg,PCNA,,1.0,#00c0c0,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_PDPN.jpg,PDPN,,1.0,#CB5352,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_PODXL.jpg,PODXL,,1.0,#76DD55,yes
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_POSTN.jpg,POSTN,,1.0,#00c080,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_PTEN.jpg,PTEN,,1.0,#80c000,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_STAT1.jpg,STAT1,,1.0,#408080,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_UMOD.jpg,UMOD,,1.0,#C96000,yes
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_VIM.jpg,VIM,,1.0,#A361C7,no
https://lundberglab.stanford.edu/Prominent/images/20240418_d1_kid_K2110291_Scan2_ZO1.jpg,ZO1,,1.0,#ffff32,no
```

- The images in that folder ( `https://lundberglab.stanford.edu/Prominent/images/` ) have been processed with the `create_pyramid.py` (located in the `util` repository folder) to generate a pyramid file structure that is also copied in the same folder. Unfortunatelly, the images are too big to be added to github, but they look like this:

![Example 3 pyramid files](./doc/doc1.jpg "Example 3 pyramid files")

- You can call the viewer just with the following URL: `https://lundberglab.stanford.edu/ellviewer/ellviewer.html?csv=[URL to your accessible metadata.csv]&resolution=15360x18720&minTileResolution=4096` ( for demo purposes, just try https://lundberglab.stanford.edu/ellviewer/ellviewer.html?csv=https://ell-vault.stanford.edu/dav/fredbn/www/ellviewer/demo3/metadata.csv&resolution=15360x18720&minTileResolution=4096 )
