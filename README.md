# DPReview Archive
A simple script to archive some part of DPReview

This `widget.py` will fetch images and info texts from DPReview Image Comparison Tool and save them into `{widget_id}. {scene_title}/{image_attributes}_{image_id}.{extension}`, e.g. `1. Studio scene/Daylight_nikon_d810_Raw_800_None_None_None_24950.nef`.

Edit line 11 to use proxy.

Uncomment line 71-74 if you want to save the request and response data for debug or other purposes.

Comment out line 82 and 87 if you only want to print image URLs out instead of downloading them.

By default, this script will only archive Studio scene(1), Video Stills Comparison(67), Raw DR: ISO-invariance(197) and Raw DR: Exposure Latitude(205). You can edit line 144 to archive images from other tools.

Here is a (hopefully) complete list of currently available tools (unique `sceneId`) on DPReview:

| widget | sceneId | sceneTitle | Note | Size | My progress |
| ------ | ------- | ---------- | ---- | ---- | -------- |
| 1 | 1 | [Studio scene](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=1) |  |  | ~70% |
| 21 | 6 | [Connect Studio Scene](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=21) | Smartphones |  |  |
| 47 | 7 | [Shadow Noise Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=47) |  | 359M | 100% |
| 67 | 9 | [Video Stills Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=67) |  | 1.2G | 100% |
| 69 | 10 | [Sony DSC-RX10 noise reduction sample](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=69) | s3Key error | 40M | 80% |
| 76 | 12 | [E-M10 Video Modes](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=76) |  | 3.1M | 100% |
| 82 | 13 | [AA Filter Simulation](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=82) | on PENTAX K-3 | 313M | 100% |
| 97 | 15 | [PowerShot G1 X II Raw Shadow Recovery](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=97) |  | 58M | 100% |
| 101 | 16 | [2014 Waterproof Real World (daylight)](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=101) |  | 21M | 100% |
| 104 | 17 | [RX100 III video modes](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=104) |  | 0 | 100% |
| 111 | 19 | [2014 Waterproof Real World (low light)](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=111) |  | 22M | 100% |
| 112 | 20 | [2014 Waterproof Studio Scene](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=112) |  | 448M | 100% |
| 119 | 22 | [A7S ISO Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=119) |  | 4.1G | 100% |
| 120 | 21 | [Panasonic Lumix DMC-FZ1000 vs Sony Cyber-shot DSC-RX10](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=120) |  | 50M | 100% |
| 121 | 23 | [Panasonic FZ1000 vs Sony RX10 real-world](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=121) |  | 50M | 100% |
| 133 | 26 | [High ISO Compared](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=133) |  | 0 | 100% |
| 137 | 27 | [ISO Compared: GH4 vs A7S](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=137) |  | 1.2G | 100% |
| 159 | 28 | [G7 X Raw Improvement](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=159) |  | 42M | 100% |
| 163 | 30 | [Compact Camera Lens Assessment](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=163) |  | 8.8G | 100% |
| 164 | 29 | [Lx100 real-world Raw DR comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=164) |  | 125M | 100% |
| 172 | 32 | [D750 Raw improvement](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=172) |  | 60M | 100% |
| 173 | 33 | [Exposure Latitude](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=173) |  | 201M | 100% |
| 178 | 36 | [Canon EOS 7D II Real-World DR](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=178) |  | 226M | 100% |
| 184 | 39 | [Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=184) |  | 1.9G | 100% |
| 191 | 40 | [Foveon VS. Bayer](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=191) |  | 0 | 100% |
| 195 | 41 | [Shutter Shock](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=195) |  | 0 | 100% |
| 197 | 43 | [Raw DR: ISO-invariance](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=197) |  | 55G | 100% |
| 201 | 44 | [Real World Dynamic Range](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=201) |  | 127M | 100% |
| 205 | 45 | [Raw DR: Exposure Latitude](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=205) |  | 63G | 100% |
| 214 | 46 | [Real World Dynamic Range](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=214) |  | 67M | 100% |
| 218 | 47 | [Mirror/Shutter Shock (on Tripod)](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=218) |  | 63G | 100% |
| 240 | 49 | [2015 Superzoom Lens Test](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=240) |  | 187M | 100% |
| 245 | 50 | [Canon PowerShot SX60 Raw vs JPEG](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=245) |  | 34M | 100% |
| 246 | 51 | [Fujifilm FinePix S1 Raw vs. JPEG](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=246) |  | 37M | 100% |
| 247 | 52 | [Zeiss Otus](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=247) |  | 705M | 100% |
| 259 | 53 | [Olympus TG-4 Raw vs JPEG](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=259) |  | 57M | 100% |
| 266 | 54 | [Sony a7R II - Real World ISO-invariance](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=266) |  | 463M | 100% |
| 275 | 55 | [Sony a7R II E-shutter](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=275) |  | 1.7G | 100% |
| 276 | 56 | [Real World Dynamic Range](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=276) |  | 414M | 100% |
| 277 | 57 | [DXO One Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=277) |  | 0 | 100% |
| 295 | 58 | [Canon 35mm f/1.4 Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=295) |  | 5.6G | 100% |
| 297 | 59 | [Canon G5 X vs Sony RX100 Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=297) |  | 2.8G | 100% |
| 304 | 60 | [Canon 100-400mm F4.5-5.6L IS USM Mark I vs Mark II comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=304) |  | 1.7G | 100% |
| 306 | 61 | [RX1RII Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=306) |  | 2.2G | 100% |
| 317 | 62 | [X70 Digital Tele-Converter Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=317) |  | 24M | 100% |
| 319 | 63 | [Fujifilm X70 Lens Shootout](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=319) |  | 379M | 100% |
| 321 | 64 | [Panasonic Lumix DMC-ZS100 lens test](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=321) |  | 672M | 100% |
| 329 | 65 | [D810 Real World DR](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=329) |  | 258M | 100% |
| 342 | 66 | [Sigma 50-100mm f/1.8 Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=342) |  | 0 | 100% |
| 359 | 68 | [Bridge Camera Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=359) |  | 1.7G | 100% |
| 362 | 70 | [Pentax K1 Pixel Shift Image Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=362) |  | 448M | 100% |
| 363 | 71 | [Pentax K1 Pixel Shift Comparisons](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=363) |  | 829M | 100% |
| 364 | 72 | [Pentax K1 Pixel Shift Dynamic Range Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=364) |  | 253M | 100% |
| 371 | 73 | [K-1 Static Subject Pixel Shift Image Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=371) |  | 436M | 100% |
| 376 | 74 | [24-70 Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=376) |  | 0 | 100% |
| 381 | 75 | [Sony FE 50mm F1.4 ZA vs 50mm F1.8 ZA](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=381) |  | 1.5G | 100% |
| 382 | 76 | [24-70 Lens Comparison (Corrected)](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=382) |  | 0 | 100% |
| 387 | 77 | [Lens Comparison test Scene](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=387) |  | 0 | 100% |
| 391 | 78 | [Sigma 30mm F1.4 DC DN C Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=391) |  | 930M | 100% |
| 399 | 79 | [Nikkor 24mm f/1.8 Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=399) |  | 1.1G | 100% |
| 400 | 80 | [Nikon 24mm F1.8 Bokeh Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=400) |  | 409M | 100% |
| 402 | 81 | [Sigma 30mm F1.4 DC DN C Bokeh Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=402) |  | 505M | 100% |
| 434 | 82 | [Sigma 12-24mm F4 Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=434) |  | 6.2G | 100% |
| 435 | 83 | [Sigma Focused Wide Open vs Focused At Aperture at 24mm](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=435) |  | 479M | 100% |
| 440 | 84 | [YI M1 4K Video Stills Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=440) |  | 0 | 100% |
| 441 | 85 | [Canon 35mm F1.4L II vs I Shootout](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=441) |  | 3.0G | 100% |
| 446 | 87 | [Canon 16-35mm F2.8L III Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=446) |  | 6.8G | 100% |
| 449 | 88 | [Canon 16-35mm F2.8L III Coma Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=449) |  | 172M | 100% |
| 451 | 86 | [Lens comparison: Panasonic FZ2500/FZ2000 vs Sony RX10 III](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=451) |  | 1.5G | 100% |
| 463 | 89 | [Sigma 85mm F1.4 Art Bokeh Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=463) |  | 1.2G | 100% |
| 466 | 90 | [Sigma 85mm F1.4 Art Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=466) |  | 1.7G | 100% |
| 467 | 91 | [a99 II Noise Test](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=467) |  | 2.5G | 100% |
| 471 | 92 | [Nikkor 105mm F1.4E ED Bokeh Test](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=471) |  | 0 | 100% |
| 472 | 93 | [Nikkor 105mm F1.4E ED Balcony Scene](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=472) |  | 0 | 100% |
| 498 | 94 | [Fujifilm GFX 50S Comparison Widget](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=498) |  | 591M | 100% |
| 507 | 96 | [Canon 18-55mm F4.0-5.6 lens assessment](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=507) |  | 114M | 100% |
| 519 | 97 | [a9 Real-World ISO-Invariance](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=519) |  | 2.8G | 100% |
| 539 | 99 | [Fujifilm X-A3 noise reduction](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=539) |  | 60M | 100% |
| 560 | 100 | [Sony a7R III Real-World ISO-invariance](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=560) |  | 2.3G | 100% |
| 566 | 101 | [Sony a7R III Real World Pixel Shift](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=566) |  | 105M | 100% |
| 573 | 102 | [Sony a7R III Comparisons](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=573) |  | 228M | 100% |
| 599 | 103 | [Pentax K-1 II Pixel Shift Comparisons](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=599) |  | 1.9G | 100% |
| 603 | 104 | [Super Resolution Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=603) |  | 87M | 100% |
| 610 | 106 | [Panasonic ZS200 vs ZS100 lens comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=610) |  | 1.7G | 100% |
| 612 | 107 | [Samsung Galaxy S9+ aperture comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=612) |  | 20M | 100% |
| 615 | 108 | [Travel Zoom Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=615) |  | 1.7G | 100% |
| 616 | 109 | [Tamron 70-210mm F4 versus Canon 70-200mm F4L II](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=616) |  | 1.9G | 100% |
| 637 | 110 | [5DIV (85mm) vs EOS R (50mm) studio scene](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=637) |  | 144M | 100% |
| 651 | 111 | [50mm lens comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=651) |  | 3.9G | 100% |
| 656 | 112 | [Canon 32mm F1.4](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=656) |  | 0 | 100% |
| 657 | 113 | [Fujifilm GFX 50R vs Nikon Z7](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=657) |  | 499M | 100% |
| 684 | 114 | [Leica Q2 Lens Comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=684) |  | 677M | 100% |
| 692 | 115 | [Canon RF 35mm F1.8](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=692) |  | 1.2G | 100% |
| 696 | 116 | [Panasonic S1R non-standard sharpening](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=696) |  | 546M | 100% |
| 704 | 118 | [Prime Lens Shootout](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=704) |  | 3.0G | 100% |
| 752 | 67 | [X100 lens comparison](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=752) |  | 1.9G | 100% |
| 812 | 119 | [Adobe Super Resolution Comparisons](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=812) |  | 357M | 100% |
| 824 | 120 | [ACR Super Resolution (2021)](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=824) |  | 0 | 100% |
| 827 | 121 | [ACR Super Resolution](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=827) |  | 0 | 100% |
| 867 | 123 | [Studio lens test](https://www.dpreview.com/reviews/image-comparison/fullscreen?widget=867) |  | 317M | 100% |


## TODO
- [ ] Add command line interface
- [ ] Adjust request rate dynamically
- [ ] ~~Async download~~ Doesn't seem helpful
- [ ] Error handling
