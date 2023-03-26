# DPReview Archive
~~A simple script to~~ archive some part of DPReview

~~This script will fetch images and info texts from DPReview Image Comparison Tool and save them into `{widget_id}. {scene_title}/{image_attributes}_{image_id}.{extension}`, e.g. `1. Studio scene/Daylight_nikon_d810_Raw_800_None_None_None_24950.nef`.~~

~~Uncomment line 62-65 if you want to save the request and response data for debug or other purposes.~~

~~Comment out line 73 and 78, uncomment line 74 and 79 if you want to print image URLs out instead of download them.~~

~~By default, this script will only archive Studio scene(1), Video Stills Comparison(67), Raw DR: ISO-invariance(197) and Raw DR: Exposure Latitude(205). You can edit line 134 to archive images from other tools, but this script may not work on some of them.~~

Here is the (hopefully) complete list of currently available tools (unique `sceneId`) on DPReview:

| widget | sceneId | sceneTitle | Note | Progress |
| ------ | ------- | ---------- | ---- | -------- |
| 1 | 1 | Studio scene |  | ~10% |
| 21 | 6 | Connect Studio Scene | Smartphones |  |
| 47 | 7 | Shadow Noise Comparison |  |  |
| 67 | 9 | Video Stills Comparison |  | 100% |
| 69 | 10 | Sony DSC-RX10 noise reduction sample |  |  |
| 76 | 12 | E-M10 Video Modes |  |  |
| 82 | 13 | AA Filter Simulation | on PENTAX K-3 |  |
| 97 | 15 | PowerShot G1 X II Raw Shadow Recovery |  |  |
| 101 | 16 | 2014 Waterproof Real World (daylight) |  |  |
| 104 | 17 | RX100 III video modes |  |  |
| 111 | 19 | 2014 Waterproof Real World (low light) |  |  |
| 112 | 20 | 2014 Waterproof Studio Scene |  |  |
| 119 | 22 | A7S ISO Comparison |  |  |
| 120 | 21 | Panasonic Lumix DMC-FZ1000 vs Sony Cyber-shot DSC-RX10 |  |  |
| 121 | 23 | Panasonic FZ1000 vs Sony RX10 real-world |  |  |
| 133 | 26 | High ISO Compared |  |  |
| 137 | 27 | ISO Compared: GH4 vs A7S |  |  |
| 159 | 28 | G7 X Raw Improvement |  |  |
| 163 | 30 | Compact Camera Lens Assessment |  |  |
| 164 | 29 | Lx100 real-world Raw DR comparison |  |  |
| 172 | 32 | D750 Raw improvement |  |  |
| 173 | 33 | Exposure Latitude |  |  |
| 178 | 36 | Canon EOS 7D II Real-World DR |  |  |
| 184 | 39 | Lens Comparison |  |  |
| 191 | 40 | Foveon VS. Bayer |  |  |
| 195 | 41 | Shutter Shock |  |  |
| 197 | 43 | Raw DR: ISO-invariance |  |  |
| 201 | 44 | Real World Dynamic Range |  |  |
| 205 | 45 | Raw DR: Exposure Latitude |  |  |
| 214 | 46 | Real World Dynamic Range |  |  |
| 218 | 47 | Mirror/Shutter Shock (on Tripod) |  |  |
| 240 | 49 | 2015 Superzoom Lens Test |  |  |
| 245 | 50 | Canon PowerShot SX60 Raw vs JPEG |  |  |
| 246 | 51 | Fujifilm FinePix S1 Raw vs. JPEG |  |  |
| 247 | 52 | Zeiss Otus |  |  |
| 259 | 53 | Olympus TG-4 Raw vs JPEG |  |  |
| 266 | 54 | Sony a7R II - Real World ISO-invariance |  |  |
| 275 | 55 | Sony a7R II E-shutter |  |  |
| 276 | 56 | Real World Dynamic Range |  |  |
| 277 | 57 | DXO One Lens Comparison |  |  |
| 295 | 58 | Canon 35mm f/1.4 Lens Comparison |  |  |
| 297 | 59 | Canon G5 X vs Sony RX100 Lens Comparison |  |  |
| 304 | 60 | Canon 100-400mm F4.5-5.6L IS USM Mark I vs Mark II comparison |  |  |
| 306 | 61 | RX1RII Lens Comparison |  |  |
| 317 | 62 | X70 Digital Tele-Converter Comparison |  |  |
| 319 | 63 | Fujifilm X70 Lens Shootout |  |  |
| 321 | 64 | Panasonic Lumix DMC-ZS100 lens test |  |  |
| 329 | 65 | D810 Real World DR |  |  |
| 342 | 66 | Sigma 50-100mm f/1.8 Comparison |  |  |
| 359 | 68 | Bridge Camera Lens Comparison |  |  |
| 362 | 70 | Pentax K1 Pixel Shift Image Comparison |  |  |
| 363 | 71 | Pentax K1 Pixel Shift Comparisons |  |  |
| 364 | 72 | Pentax K1 Pixel Shift Dynamic Range Comparison |  |  |
| 371 | 73 | K-1 Static Subject Pixel Shift Image Comparison |  |  |
| 376 | 74 | 24-70 Comparison |  |  |
| 381 | 75 | Sony FE 50mm F1.4 ZA vs 50mm F1.8 ZA |  |  |
| 382 | 76 | 24-70 Lens Comparison (Corrected) |  |  |
| 387 | 77 | Lens Comparison test Scene |  |  |
| 391 | 78 | Sigma 30mm F1.4 DC DN C Comparison |  |  |
| 399 | 79 | Nikkor 24mm f/1.8 Lens Comparison |  |  |
| 400 | 80 | Nikon 24mm F1.8 Bokeh Comparison |  |  |
| 402 | 81 | Sigma 30mm F1.4 DC DN C Bokeh Comparison |  |  |
| 434 | 82 | Sigma 12-24mm F4 Lens Comparison |  |  |
| 435 | 83 | Sigma Focused Wide Open vs Focused At Aperture at 24mm |  |  |
| 440 | 84 | YI M1 4K Video Stills Lens Comparison |  |  |
| 441 | 85 | Canon 35mm F1.4L II vs I Shootout |  |  |
| 446 | 87 | Canon 16-35mm F2.8L III Lens Comparison |  |  |
| 449 | 88 | Canon 16-35mm F2.8L III Coma Comparison |  |  |
| 451 | 86 | Lens comparison: Panasonic FZ2500/FZ2000 vs Sony RX10 III |  |  |
| 463 | 89 | Sigma 85mm F1.4 Art Bokeh Comparison |  |  |
| 466 | 90 | Sigma 85mm F1.4 Art Lens Comparison |  |  |
| 467 | 91 | a99 II Noise Test |  |  |
| 471 | 92 | Nikkor 105mm F1.4E ED Bokeh Test |  |  |
| 472 | 93 | Nikkor 105mm F1.4E ED Balcony Scene |  |  |
| 498 | 94 | Fujifilm GFX 50S Comparison Widget |  |  |
| 507 | 96 | Canon 18-55mm F4.0-5.6 lens assessment |  |  |
| 519 | 97 | a9 Real-World ISO-Invariance |  |  |
| 539 | 99 | Fujifilm X-A3 noise reduction |  |  |
| 560 | 100 | Sony a7R III Real-World ISO-invariance |  |  |
| 566 | 101 | Sony a7R III Real World Pixel Shift |  |  |
| 573 | 102 | Sony a7R III Comparisons |  |  |
| 599 | 103 | Pentax K-1 II Pixel Shift Comparisons |  |  |
| 603 | 104 | Super Resolution Comparison |  |  |
| 610 | 106 | Panasonic ZS200 vs ZS100 lens comparison |  |  |
| 612 | 107 | Samsung Galaxy S9+ aperture comparison |  |  |
| 615 | 108 | Travel Zoom Lens Comparison |  |  |
| 616 | 109 | Tamron 70-210mm F4 versus Canon 70-200mm F4L II |  |  |
| 637 | 110 | 5DIV (85mm) vs EOS R (50mm) studio scene |  |  |
| 651 | 111 | 50mm lens comparison |  |  |
| 656 | 112 | Canon 32mm F1.4 |  |  |
| 657 | 113 | Fujifilm GFX 50R vs Nikon Z7 |  |  |
| 684 | 114 | Leica Q2 Lens Comparison |  |  |
| 692 | 115 | Canon RF 35mm F1.8 |  |  |
| 696 | 116 | Panasonic S1R non-standard sharpening |  |  |
| 704 | 118 | Prime Lens Shootout |  |  |
| 752 | 67 | X100 lens comparison |  |  |
| 812 | 119 | Adobe Super Resolution Comparisons |  |  |
| 824 | 120 | ACR Super Resolution (2021) |  |  |
| 827 | 121 | ACR Super Resolution |  |  |
| 867 | 123 | Studio lens test |  |  |


## TODO
- [ ] Add command line interface
- [ ] Adjust request rate dynamically
- [ ] ~~Async download~~ Doesn't seem helpful
- [ ] Error handling
