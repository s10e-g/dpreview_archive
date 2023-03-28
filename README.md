# DPReview Archive
A simple script to archive some part of DPReview

This script will fetch images and info texts from DPReview Image Comparison Tool and save them into `{widget_id}. {scene_title}/{image_attributes}_{image_id}.{extension}`, e.g. `1. Studio scene/Daylight_nikon_d810_Raw_800_None_None_None_24950.nef`.

Edit line 11 to use proxy.

Uncomment line 71-74 if you want to save the request and response data for debug or other purposes.

Comment out line 82 and 87 if you only want to print image URLs out instead of download them.

By default, this script will only archive Studio scene(1), Video Stills Comparison(67), Raw DR: ISO-invariance(197) and Raw DR: Exposure Latitude(205). You can edit line 143 to archive images from other tools, but this script may not work on some of them.

Here is a (hopefully) complete list of currently available tools (unique `sceneId`) on DPReview:

| widget | sceneId | sceneTitle | Note | Size | My progress |
| ------ | ------- | ---------- | ---- | ---- | -------- |
| 1 | 1 | Studio scene |  |  | ~70% |
| 21 | 6 | Connect Studio Scene | Smartphones |  |  |
| 47 | 7 | Shadow Noise Comparison |  | 359M | 100% |
| 67 | 9 | Video Stills Comparison |  | 1.2G | 100% |
| 69 | 10 | Sony DSC-RX10 noise reduction sample | s3Key error | 40M | 80% |
| 76 | 12 | E-M10 Video Modes |  | 3.1M | 100% |
| 82 | 13 | AA Filter Simulation | on PENTAX K-3 | 313M | 100% |
| 97 | 15 | PowerShot G1 X II Raw Shadow Recovery |  | 58M | 100% |
| 101 | 16 | 2014 Waterproof Real World (daylight) |  | 21M | 100% |
| 104 | 17 | RX100 III video modes |  | 0 | 100% |
| 111 | 19 | 2014 Waterproof Real World (low light) |  | 22M | 100% |
| 112 | 20 | 2014 Waterproof Studio Scene |  | 448M | 100% |
| 119 | 22 | A7S ISO Comparison |  | 4.1G | 100% |
| 120 | 21 | Panasonic Lumix DMC-FZ1000 vs Sony Cyber-shot DSC-RX10 |  | 50M | 100% |
| 121 | 23 | Panasonic FZ1000 vs Sony RX10 real-world |  | 50M | 100% |
| 133 | 26 | High ISO Compared |  | 0 | 100% |
| 137 | 27 | ISO Compared: GH4 vs A7S |  | 1.2G | 100% |
| 159 | 28 | G7 X Raw Improvement |  | 42M | 100% |
| 163 | 30 | Compact Camera Lens Assessment |  | 8.8G | 100% |
| 164 | 29 | Lx100 real-world Raw DR comparison |  | 125M | 100% |
| 172 | 32 | D750 Raw improvement |  | 60M | 100% |
| 173 | 33 | Exposure Latitude |  | 201M | 100% |
| 178 | 36 | Canon EOS 7D II Real-World DR |  | 226M | 100% |
| 184 | 39 | Lens Comparison |  | 1.9G | 100% |
| 191 | 40 | Foveon VS. Bayer |  | 0 | 100% |
| 195 | 41 | Shutter Shock |  | 0 | 100% |
| 197 | 43 | Raw DR: ISO-invariance |  | 55G | 100% |
| 201 | 44 | Real World Dynamic Range |  | 127M | 100% |
| 205 | 45 | Raw DR: Exposure Latitude |  | 63G | 100% |
| 214 | 46 | Real World Dynamic Range |  | 67M | 100% |
| 218 | 47 | Mirror/Shutter Shock (on Tripod) |  | 63G | 100% |
| 240 | 49 | 2015 Superzoom Lens Test |  | 187M | 100% |
| 245 | 50 | Canon PowerShot SX60 Raw vs JPEG |  | 34M | 100% |
| 246 | 51 | Fujifilm FinePix S1 Raw vs. JPEG |  | 37M | 100% |
| 247 | 52 | Zeiss Otus |  | 705M | 100% |
| 259 | 53 | Olympus TG-4 Raw vs JPEG |  | 57M | 100% |
| 266 | 54 | Sony a7R II - Real World ISO-invariance |  | 463M | 100% |
| 275 | 55 | Sony a7R II E-shutter |  | 1.7G | 100% |
| 276 | 56 | Real World Dynamic Range |  | 414M | 100% |
| 277 | 57 | DXO One Lens Comparison |  | 0 | 100% |
| 295 | 58 | Canon 35mm f/1.4 Lens Comparison |  | 5.6G | 100% |
| 297 | 59 | Canon G5 X vs Sony RX100 Lens Comparison |  | 2.8G | 100% |
| 304 | 60 | Canon 100-400mm F4.5-5.6L IS USM Mark I vs Mark II comparison |  | 1.7G | 100% |
| 306 | 61 | RX1RII Lens Comparison |  | 2.2G | 100% |
| 317 | 62 | X70 Digital Tele-Converter Comparison |  | 24M | 100% |
| 319 | 63 | Fujifilm X70 Lens Shootout |  | 379M | 100% |
| 321 | 64 | Panasonic Lumix DMC-ZS100 lens test |  | 672M | 100% |
| 329 | 65 | D810 Real World DR |  | 258M | 100% |
| 342 | 66 | Sigma 50-100mm f/1.8 Comparison |  | 0 | 100% |
| 359 | 68 | Bridge Camera Lens Comparison |  | 1.7G | 100% |
| 362 | 70 | Pentax K1 Pixel Shift Image Comparison |  | 448M | 100% |
| 363 | 71 | Pentax K1 Pixel Shift Comparisons |  | 829M | 100% |
| 364 | 72 | Pentax K1 Pixel Shift Dynamic Range Comparison |  | 253M | 100% |
| 371 | 73 | K-1 Static Subject Pixel Shift Image Comparison |  | 436M | 100% |
| 376 | 74 | 24-70 Comparison |  | 0 | 100% |
| 381 | 75 | Sony FE 50mm F1.4 ZA vs 50mm F1.8 ZA |  | 1.5G | 100% |
| 382 | 76 | 24-70 Lens Comparison (Corrected) |  | 0 | 100% |
| 387 | 77 | Lens Comparison test Scene |  | 0 | 100% |
| 391 | 78 | Sigma 30mm F1.4 DC DN C Comparison |  | 930M | 100% |
| 399 | 79 | Nikkor 24mm f/1.8 Lens Comparison |  | 1.1G | 100% |
| 400 | 80 | Nikon 24mm F1.8 Bokeh Comparison |  | 409M | 100% |
| 402 | 81 | Sigma 30mm F1.4 DC DN C Bokeh Comparison |  | 505M | 100% |
| 434 | 82 | Sigma 12-24mm F4 Lens Comparison |  | 6.2G | 100% |
| 435 | 83 | Sigma Focused Wide Open vs Focused At Aperture at 24mm |  | 479M | 100% |
| 440 | 84 | YI M1 4K Video Stills Lens Comparison |  | 0 | 100% |
| 441 | 85 | Canon 35mm F1.4L II vs I Shootout |  | 3.0G | 100% |
| 446 | 87 | Canon 16-35mm F2.8L III Lens Comparison |  | 6.8G | 100% |
| 449 | 88 | Canon 16-35mm F2.8L III Coma Comparison |  | 172M | 100% |
| 451 | 86 | Lens comparison: Panasonic FZ2500/FZ2000 vs Sony RX10 III |  | 1.5G | 100% |
| 463 | 89 | Sigma 85mm F1.4 Art Bokeh Comparison |  | 1.2G | 100% |
| 466 | 90 | Sigma 85mm F1.4 Art Lens Comparison |  | 1.7G | 100% |
| 467 | 91 | a99 II Noise Test |  | 2.5G | 100% |
| 471 | 92 | Nikkor 105mm F1.4E ED Bokeh Test |  | 0 | 100% |
| 472 | 93 | Nikkor 105mm F1.4E ED Balcony Scene |  | 0 | 100% |
| 498 | 94 | Fujifilm GFX 50S Comparison Widget |  | 591M | 100% |
| 507 | 96 | Canon 18-55mm F4.0-5.6 lens assessment |  | 114M | 100% |
| 519 | 97 | a9 Real-World ISO-Invariance |  | 2.8G | 100% |
| 539 | 99 | Fujifilm X-A3 noise reduction |  | 60M | 100% |
| 560 | 100 | Sony a7R III Real-World ISO-invariance |  | 2.3G | 100% |
| 566 | 101 | Sony a7R III Real World Pixel Shift |  | 105M | 100% |
| 573 | 102 | Sony a7R III Comparisons |  | 228M | 100% |
| 599 | 103 | Pentax K-1 II Pixel Shift Comparisons |  | 1.9G | 100% |
| 603 | 104 | Super Resolution Comparison |  | 87M | 100% |
| 610 | 106 | Panasonic ZS200 vs ZS100 lens comparison |  | 1.7G | 100% |
| 612 | 107 | Samsung Galaxy S9+ aperture comparison |  | 20M | 100% |
| 615 | 108 | Travel Zoom Lens Comparison |  | 1.7G | 100% |
| 616 | 109 | Tamron 70-210mm F4 versus Canon 70-200mm F4L II |  | 1.9G | 100% |
| 637 | 110 | 5DIV (85mm) vs EOS R (50mm) studio scene |  | 144M | 100% |
| 651 | 111 | 50mm lens comparison |  | 3.9G | 100% |
| 656 | 112 | Canon 32mm F1.4 |  | 0 | 100% |
| 657 | 113 | Fujifilm GFX 50R vs Nikon Z7 |  | 499M | 100% |
| 684 | 114 | Leica Q2 Lens Comparison |  | 677M | 100% |
| 692 | 115 | Canon RF 35mm F1.8 |  | 1.2G | 100% |
| 696 | 116 | Panasonic S1R non-standard sharpening |  | 546M | 100% |
| 704 | 118 | Prime Lens Shootout |  | 3.0G | 100% |
| 752 | 67 | X100 lens comparison |  | 1.9G | 100% |
| 812 | 119 | Adobe Super Resolution Comparisons |  | 357M | 100% |
| 824 | 120 | ACR Super Resolution (2021) |  | 0 | 100% |
| 827 | 121 | ACR Super Resolution |  | 0 | 100% |
| 867 | 123 | Studio lens test |  | 317M | 100% |


## TODO
- [ ] Add command line interface
- [ ] Adjust request rate dynamically
- [ ] ~~Async download~~ Doesn't seem helpful
- [ ] Error handling
