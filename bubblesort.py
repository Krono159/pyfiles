def sort(owo):
    for n in range(len(owo)-1,0,-1):
        for i in range(n):
            if owo[i] > owo[i+1]:
                owo[i], owo[i+1] = owo[i+1],owo[i]
owo = [4290, 4973, 3009, 4721, 3282, 2985, 3880, 730, 37, 3471, 2248, 2537, 3124, 751, 2863, 2326, 3918, 2891, 1366, 153, 1572, 4085, 1383, 4039, 2187, 2879, 4594, 2363, 3976, 3018, 2482, 4793, 1254, 2870, 4668, 1040, 1594, 233, 4514, 1999, 4793, 1463, 4306, 1377, 3426, 1166, 117, 2080, 4290, 3760, 4144, 1500, 370, 298, 4534, 2378, 2620, 2172, 4525, 3559, 68, 2895, 1745, 3841, 2386, 1745, 2394, 2847, 4538, 334, 3403, 884, 2214, 2414, 4276, 3138, 253, 2813, 2135, 568, 379, 2233, 1111, 1892, 4395, 1942, 2234, 2566, 3260, 3321, 4259, 1300, 3196, 1603, 1267, 373, 4560, 2499, 2750, 2679, 4725, 3107, 734, 2708, 3803, 314, 3069, 3725, 3276, 3441, 109, 3962, 2721, 4529, 3482, 4932, 2566, 4661, 2578, 60, 1076, 2327, 1620, 4775, 137, 976, 3750, 514, 1594, 1719, 81, 4483, 858, 2129, 1871, 3389, 4904, 1057, 2573, 574, 2177, 636, 2951, 3169, 7, 1808, 1409, 4488, 2382, 2155, 3201, 4995, 4129, 2435, 949, 1972, 929, 1373, 13, 2031, 4937, 2271, 2075, 2809, 2799, 659, 769, 2509, 4500, 144, 1520, 4399, 1665, 2935, 1230, 230, 3830, 2237, 4412, 2799, 1062, 657, 2015, 1214, 2002, 4762, 3875, 472, 2411, 2962, 3232, 2246, 4494, 1620, 500, 1315, 1805, 3320, 3458, 1363, 2700, 519, 1311, 4868, 692, 2701, 1036, 993, 2276, 3669, 2158, 85, 1266, 2485, 1053, 886, 2297, 3603, 4062, 4498, 1415, 3038, 451, 1481, 4213, 2055, 698, 411, 424, 4515, 4785, 2390, 3435, 1262, 2516, 4439, 4618, 4391, 3735, 4939, 4097, 4481, 4959, 4923, 2433, 2, 3391, 2399, 4470, 2461, 4307, 360, 2391, 1583, 738, 1363, 516, 1804, 2578, 1609, 1166, 552, 127, 1723, 1118, 2617, 2191, 4422, 3372, 157, 4140, 3883, 1892, 3931, 3100, 2260, 4022, 1668, 953, 4982, 2261, 4703, 3316, 4677, 2571, 198, 3117, 468, 956, 4781, 147, 2211, 4503, 3866, 4863, 3826, 1379, 511, 2550, 4976, 2502, 3130, 1245, 2238, 2503, 1547, 2729, 38, 562, 2853, 2162, 2134, 2093, 2119, 1883, 2526, 2209, 4270, 1715, 447, 1968, 2869, 4996, 2456, 2521, 3889, 3565, 4963, 3580, 2391, 1435, 2941, 2811, 2525, 4780, 4070, 2811, 4614, 3760, 4852, 1990, 1401, 2701, 4208, 4770, 4779, 3223, 4812, 95, 147, 3676, 4440, 4394, 2121, 2516, 1069, 3772, 608, 4497, 2358, 4662, 2268, 3019, 4731, 2133, 106, 4749, 4559, 4174, 3260, 4620, 4359, 2971, 3683, 3694, 3627, 234, 4432, 4813, 4750, 899, 4331, 3253, 37, 3870, 3862, 83, 3127, 2258, 4640, 2077, 1315, 250, 945, 4543, 2055, 4463, 2533, 2540, 2601, 1281, 4949, 1932, 1278, 4422, 1931, 3933, 2219, 3288, 1387, 2743, 1913, 319, 1817, 3663, 1683, 4748, 2734, 3312, 3434, 1881, 476, 1304, 3500, 4158, 3332, 1172, 3215, 2262, 1971, 4376, 401, 1079, 2798, 3506, 460, 2240, 3557, 3100, 1027, 4749, 2887, 401, 2276, 745, 1569, 2606, 4729, 2027, 482, 1353, 3122, 515, 3185, 4388, 1510, 4202, 1983, 3358, 904, 4452, 2158, 1949, 1346, 4256, 2549, 726, 3908, 152, 1158, 327, 4859, 3817, 2089, 435, 678, 3065, 141, 4276, 3105, 282, 1386, 4974, 88, 1208, 734, 1743, 3595, 584, 3774, 3121, 1906, 4170, 2943, 2023, 2287, 692, 4103, 3254, 2854, 531, 274, 2710, 1924, 1923, 3744, 2368, 871, 290, 1956, 3016, 2478, 2323, 2892, 2978, 102, 1084, 259, 399, 4197, 4390, 426, 800, 4985, 4762, 3704, 2149, 2279, 4335, 1100, 966, 408, 1255, 4715, 2895, 3358, 973, 95, 467, 292, 903, 2103, 3975, 3634, 313, 3103, 38, 1143, 2925, 3750, 329, 723, 642, 132, 837, 2039, 4900, 1793, 3075, 4249, 4122, 3325, 4730, 196, 1963, 2170, 3819, 4819, 1587, 4911, 1363, 4059, 3455, 3989, 1560, 3268, 4026, 1164, 3921, 427, 1920, 2648, 2396, 3081, 4866, 1168, 4419, 3316, 2882, 2460, 2305, 4219, 565, 1886, 759, 694, 525, 4357, 2306, 2926, 3862, 2813, 2021, 2988, 3718, 2564, 4871, 3779, 1375, 3200, 1047, 2690, 834, 2820, 4413, 2410, 1381, 3941, 2154, 1712, 3639, 4584, 189, 1748, 3009, 1265, 4692, 2461, 4286, 4380, 1176, 3330, 1830, 2456, 2369, 4337, 1043, 4964, 4509, 195, 2931, 4737, 1597, 515, 3887, 138, 4960, 3895, 4079, 3229, 4734, 821, 524, 397, 2281, 2968, 3091, 4654, 4378, 4652, 4604, 893, 1025, 3985, 4683, 1986, 1561, 3629, 4931, 219, 2573, 130, 1410, 3164, 552, 3691, 135, 4297, 1517, 4390, 3969, 4123, 2401, 3041, 581, 4243, 922, 3943, 3980, 3437, 641, 1883, 4600, 3537, 1315, 3502, 3477, 1789, 2323, 1451, 4262, 115, 3918, 2043, 1387, 2979, 3410, 237, 157, 3951, 1088, 4532, 4962, 2847, 4578, 2683, 2631, 4490, 1508, 1010, 1648, 3244, 4558, 4325, 2950, 4450, 2111, 3964, 3896, 1938, 3004, 3717, 2075, 2052, 3845, 3305, 66, 1497, 975, 2549, 4329, 1072, 2801, 4296, 934, 1635, 2209, 3610, 887, 3172, 847, 2043, 4520, 4087, 3476, 3455, 4627, 1051, 2293, 2450, 99, 3694, 3819, 3924, 2739, 3666, 924, 4545, 4524, 2280, 3718, 2081, 2290, 4424, 4038, 3838, 4981, 3408, 1318, 5000, 2345, 1412, 2449, 2453, 3767, 153, 4875, 783, 1694, 1160, 2531, 3452, 1370, 2698, 1947, 1660, 2389, 2449, 1058, 1445, 1035, 113, 168, 4275, 1701, 4774, 3983, 1845, 4028, 1943, 164, 4536, 2204, 872, 1068, 2490, 2961, 2685, 4413, 1391, 2429, 3698, 2590, 475, 4359, 3626, 2814, 1640, 1063, 4278, 1130, 1475, 394, 1631, 3776, 2771, 3456, 2911, 3468, 4489, 453, 1193, 2225, 4201, 779, 1132, 2843, 931, 1469, 343, 3572, 2102, 3733, 1377, 26, 223, 3445, 1016, 1337, 4105, 3722, 4842, 2573, 3291, 905, 2912, 233, 2016, 2117, 3425, 3052, 4649, 3861, 668, 2044, 2379, 724, 993, 4290, 3446, 3253, 4362, 3016, 4098, 2210, 1517, 2473, 4307, 2398, 2772, 2553, 4765, 1006, 978, 3120, 4503, 1216, 4099, 1794, 4527, 1508, 3405, 1903, 307, 1903, 4403, 789, 3573, 1829, 1088, 1327, 959, 1907, 886, 1857, 2738, 992, 3533, 1037, 1770, 1498, 2311, 157, 1781, 2023, 4769, 1680, 1599, 4452, 2915, 2224, 1567, 477, 4245, 4277, 3422, 405, 4858, 2787, 2126, 4256, 4707, 3535, 3519, 863, 596, 4332, 1917, 4442, 4229, 3891, 4609, 3414, 1750, 3286, 1073, 2744, 4871, 3164, 4229, 1153, 788, 4495, 2416, 4784, 1421, 1512, 2737, 1240, 2020, 894, 571, 3922, 3915, 3284, 2017, 3140, 2410, 3193, 1856, 1245, 4369, 1831, 2299, 3985, 4804, 1494, 4131, 3635, 2473, 4436, 2072, 2050, 3406, 2856, 2571, 4321, 3672, 2243, 325, 4838, 4242, 4702, 1176, 4042, 3382, 4660, 4380, 3451, 1488, 2275, 1993, 3991, 4911, 807, 2448, 3989, 1465, 3076, 904, 4014, 1829, 1596, 4208, 1005, 3787, 4443, 3290, 3001, 3667, 258, 1553, 480, 3792, 3269, 818, 2211, 4708, 4670, 873, 1051, 3061, 2629, 4411, 4998, 980, 1017, 3816, 1111, 2805, 1973, 4687, 3784, 1701, 4383, 1934, 42, 4203, 2569, 508, 407, 1932, 3606, 4861, 585, 3166, 3793, 3658, 2812, 3560, 359, 3612, 1372, 1452, 18, 3340, 2628, 3059, 4183, 3040, 1772, 1249, 1081, 3742, 1470, 4522, 784, 217, 3288, 4770, 4659, 4208, 2731, 4550, 4337, 4234, 1195, 2029, 4945, 3716, 2975, 1896, 4428, 4772, 3685, 3989, 3891, 675, 1729, 4042, 4463, 189, 2268, 51, 2630, 2953, 719, 2295, 4185, 666, 337, 1859, 3035, 578, 34, 4172, 612, 4789, 3961, 1533, 2851, 4376, 4489, 3713, 3277, 4798, 4840, 91, 3310, 3796, 2252, 2120, 1451, 1718, 2871, 3794, 1570, 3712, 868, 1753, 1898, 2235, 4866, 4764, 2115, 2555, 2855, 99, 902, 404, 2964, 1148, 1045, 4178, 4816, 238, 91, 3324, 353, 832, 572, 4370, 3857, 1257, 4276, 1905, 3570, 1180, 2204, 4649, 610, 73, 4946, 2319, 2786, 3877, 1864, 1587, 3701, 1498, 4433, 905, 3006, 2926, 339, 1930, 2308, 1146, 2399, 2920, 794, 2537, 2611, 3765, 2736, 1403, 3287, 2678, 2323, 3648, 1049, 3932, 513, 1960, 980, 4561, 4767, 4261, 293, 4551, 1091, 3650, 1085, 3358, 3117, 2903, 1171, 4657, 555, 4914, 4449, 2432, 4062, 2246, 1371, 2916, 1390, 3792, 3892, 3539, 1159, 4657, 1166, 109, 263, 3600, 3448, 4006, 1729, 137, 4131, 1332, 672, 1296, 1916, 3773, 2553, 2769, 4023, 3420, 2497, 2291, 3857, 2509, 235, 2920, 1388, 1528, 1102, 400, 4139, 2155, 3653, 2947, 4444, 1366, 4710, 4393, 2012, 3363, 2399, 2099, 4375, 2338, 1006, 3683, 4016, 4598, 1370, 4895, 3866, 4265, 4389, 2225, 4015, 1541, 1343, 1499, 4995, 1657, 3570, 4883, 4994, 2745, 979, 3242, 1278, 1017, 38, 4334, 2294, 4083, 3354, 2833, 2184, 2386, 1654, 3786, 2456, 845, 4207, 1204, 4370, 2848, 1625, 2115, 1338, 4443, 2004, 315, 2600, 2439, 714, 4172, 4867, 3659, 2018, 3880, 884, 1601, 2346, 329, 387, 220, 2327, 4763, 473, 1873, 3124, 745, 4277, 2217, 1819, 3869, 122, 3731, 197, 3748, 1875, 2339, 2533, 1227, 1497, 2654, 295, 2117, 4587, 136, 3401, 1506, 4247, 679, 2503, 730, 2958, 2644, 3916, 4245, 4685, 509, 1670, 4952, 2497, 231, 1396, 164, 3452, 4004, 2448, 3897, 4944, 1148, 3974, 2596, 4887, 3812, 1512, 4648, 3856, 3117, 2016, 1199, 1619, 3849, 3045, 2291, 4420, 4874, 3976, 3719, 3082, 235, 259, 184, 4003, 856, 2742, 1003, 592, 621, 4060, 3039, 837, 4320, 4728, 2698, 3866, 3611, 86, 2272, 534, 4820, 603, 3828, 3741, 336, 991, 4653, 2198, 4339, 430, 2565, 709, 3449, 4722, 768, 3303, 4035, 1554, 437, 1311, 1637, 3888, 2236, 1069, 3410, 4656, 513, 1607, 3560, 1291, 4097, 4089, 3485, 1795, 1636, 3410, 2143, 423, 1375, 2228, 1358, 4539, 2947, 2555, 3499, 3794, 1712, 2873, 961, 88, 4541, 1670, 3810, 4700, 918, 3130, 2990, 2593, 1497, 501, 2969, 3427, 640, 75, 4979, 3805, 991, 3803, 1283, 2216, 2656, 4541, 4982, 2969, 4639, 1129, 3951, 3086, 1072, 2333, 234, 1813, 360, 3619, 1753, 2191, 4295, 2900, 655, 161, 4831, 2523, 4142, 3974, 363, 1375, 810, 3419, 396, 15, 3764, 1960, 2218, 332, 2208, 2249, 2458, 753, 4576, 1600, 1302, 4067, 1593, 2709, 1582, 3293, 4951, 2278, 730, 4755, 2125, 3315, 412, 1218, 688, 2476, 1917, 3709, 3828, 2492, 1953, 721, 2302, 3181, 4406, 3006, 2127, 706, 3124, 3355, 4008, 2007, 2392, 38, 701, 1407, 2606, 1565, 1321, 59, 2825, 825, 3761, 2386, 1159, 3786, 3201, 4512, 1369, 4554, 2259, 1009, 504, 1830, 4146, 2282, 2776, 3828, 610, 3255, 34, 1104, 4121, 657, 3958, 4054, 4741, 1718, 2011, 2632, 663, 548, 3362, 2525, 3549, 4027, 1550, 1004, 1756, 3989, 4206, 4422, 2195, 3394, 1941, 2241, 4134, 2588, 366, 2187, 3831, 1146, 4618, 3273, 457, 2748, 3197, 3303, 4534, 3365, 4943, 2497, 1335, 4941, 3713, 1185, 3274, 4344, 398, 2365, 3692, 4832, 3052, 4508, 889, 2785, 462, 4475, 3470, 260, 3006, 2246, 4837, 249, 879, 3223, 2926, 2624, 1392, 1881, 652, 1831, 3423, 517, 3896, 2917, 361, 1996, 1976, 243, 3298, 631, 2509, 4629, 2553, 444, 4995, 1858, 3830, 3947, 3792, 1379, 1501, 865, 646, 877, 2295, 1361, 3631, 1886, 524, 2235, 3543, 4546, 4323, 1024, 3070, 1886, 1567, 3479, 2242, 4577, 1400, 1213, 3343, 1825, 4074, 4560, 3455, 2047, 2816, 4787, 3424, 1106, 4487, 576, 4047, 4776, 2545, 3817, 530, 4900, 500, 2771, 1804, 4510, 4253, 1973, 4522, 2484, 3439, 1385, 4099, 4440, 203, 1595, 2194, 3416, 450, 2341, 3972, 3539, 4483, 4784, 874, 2916, 279, 3524, 3691, 4260, 4677, 1431, 2738, 983, 2400, 2394, 3851, 1127, 1116, 4792, 4122, 4349, 1985, 2183, 2780, 2995, 3434, 4896, 759, 4763, 2948, 2107, 3862, 2404, 1988, 3346, 4619, 596, 3688, 2208, 2102, 688, 1526, 1271, 4566, 4155, 697, 2248, 2856, 3930, 1346, 4237, 2666, 4345, 78, 3705, 3963, 304, 2277, 3766, 4534, 2930, 3241, 1097, 4059, 3099, 1608, 2515, 3905, 4723, 3056, 346, 2635, 3290, 377, 4528, 379, 2569, 726, 2300, 2876, 4301, 1430, 1757, 272, 3912, 1545, 4996, 763, 2610, 1770, 1537, 450, 4447, 2918, 1625, 1039, 3533, 896, 2314, 3577, 4213, 2071, 3507, 2755, 1203, 1927, 3618, 4929, 2618, 2152, 1124, 4695, 2948, 43, 2062, 1251, 3489, 2529, 3391, 2425, 1636, 4907, 969, 873, 4877, 2665, 1328, 2156, 3323, 2973, 418, 4894, 3197, 740, 1645, 4070, 833, 2472, 1729, 4054, 107, 4896, 3637, 2880, 4480, 1248, 918, 4978, 2855, 3322, 2780, 3487, 4915, 2049, 2233, 1260, 4791, 3053, 2860, 4060, 4488, 900, 4632, 4945, 4171, 3025, 52, 1354, 3175, 4016, 3246, 125, 1800, 821, 1953, 1150, 1235, 765, 2028, 4848, 932, 2531, 3241, 4029, 1463, 1581, 2395, 902, 2175, 1626, 3894, 785, 4597, 1729, 4915, 2767, 426, 1127, 2622, 2517, 668, 243, 4149, 2121, 1235, 755, 1867, 4264, 3535, 3262, 966, 2644, 538, 2552, 4805, 1978, 3254, 2851, 3985, 1719, 4681, 2064, 429, 1354, 3316, 3007, 388, 4835, 1394, 1357, 1726, 533, 4310, 973, 3700, 633, 1967, 4680, 4294, 2829, 2449, 1447, 4143, 3616, 2924, 556, 3352, 391, 3469, 4200, 119, 3104, 4015, 2482, 2796, 3114, 740, 3105, 2795, 4218, 1982, 3997, 209, 2609, 275, 3952, 1896, 1488, 3514, 1555, 221, 21, 4506, 2677, 3306, 949, 2022, 4185, 4372, 2771, 675, 2601, 13, 4352, 2468, 549, 1618, 2475, 226, 596, 2255, 4844, 4768, 4035, 1418, 906, 2790, 3220, 1826, 1841, 3139, 1677, 3512, 2598, 1628, 3228, 4877, 1561, 2870, 877, 3529, 2796, 2436, 4692, 2758, 2486, 4871, 4132, 4725, 1765, 4199, 4261, 1176, 3794, 604, 810, 1923, 1528, 1397, 4989, 1780, 1908, 4297, 378, 1351, 1204, 45, 2304, 1212, 4340, 2194, 1991, 3417, 2121, 1971, 4074, 3478, 3847, 3701, 1166, 1487, 1363, 3354, 3845, 2918, 1346, 1823, 749, 4134, 788, 1920, 2368, 3719, 3780, 969, 3040, 2691, 602, 1907, 3364, 231, 1271, 182, 1805, 4848, 172, 1441, 4240, 1476, 1652, 4818, 2739, 3268, 4343, 3827, 4501, 4380, 186, 2701, 966, 629, 2308, 1662, 4948, 2998, 625, 2278, 3255, 4932, 3701, 4004, 4581, 355, 4039, 3502, 1065, 107, 3666, 4325, 1465, 816, 2977, 1889, 773, 3671, 1137, 1022, 3771, 308, 1318, 4147, 4106, 4111, 2085, 1835, 303, 2534, 928, 4505, 3699, 1306, 3138, 3221, 3052, 3980, 4867, 2509, 3952, 3850, 2321, 4449, 917, 1179, 3367, 4296, 1138, 2478, 1958, 3087, 113, 846, 3972, 3125, 2020, 1780, 1655, 1254, 3916, 3161, 3032, 677, 2434, 1867, 1995, 512, 4098, 35, 465, 2772, 626, 3126, 2786, 2844, 4500, 1152, 332, 370, 705, 1052, 4247, 3482, 1347, 1007, 4351, 1211, 802, 4142, 3540, 2285, 1394, 2521, 1453, 3222, 1047, 2588, 3154, 2369, 4281, 254, 1310, 4946, 973, 4947, 2072, 174, 1182, 1605, 4422, 1606, 350, 4766, 4032, 3641, 3450, 1834, 114, 1362, 2573, 2506, 696, 2256, 1547, 4565, 3486, 1944, 876, 4703, 2432, 603, 1758, 3345, 741, 1643, 3802, 1803, 1187, 1966, 1269, 3386, 2288, 4547, 919, 2825, 3212, 3737, 4994, 4244, 3136, 2163, 326, 2478, 1541, 2112, 355, 3700, 4583, 1959, 175, 3062, 2733, 3751, 2364, 2294, 3243, 41, 2091, 4527, 2691, 4028, 1603, 2235, 1197, 1086, 2368, 1119, 2636, 4500, 4261, 4439, 932, 2208, 334, 4259, 1231, 960, 2192, 1791, 386, 351, 3279, 1418, 3111, 3717, 3144, 4939, 250, 3474, 4802, 4115, 3543, 2633, 1738, 2564, 4521, 1206, 4247, 269, 3046, 4776, 3475, 728, 279, 2780, 1895, 431, 3195, 2688, 2708, 4746, 4575, 1632, 4486, 4245, 4023, 4704, 61, 2440, 4454, 2775, 1047, 4295, 2254, 880, 3528, 752, 2700, 1724, 4298, 2443, 3302, 4407, 4336, 3452, 605, 94, 3794, 1985, 3592, 4240, 3958, 4397, 3374, 3696, 2182, 2119, 3035, 1843, 4910, 608, 374, 2532, 3944, 1579, 3094, 485, 77, 1087, 1673, 416, 654, 3662, 1994, 2604, 2247, 510, 2030, 4574, 4816, 4252, 947, 2498, 1813, 304, 2310, 1587, 3551, 406, 772, 2975, 3889, 4356, 4969, 1299, 3410, 3882, 4772, 2601, 941, 3911, 221, 3346, 18, 4046, 1146, 2013, 3850, 1000, 2694, 1121, 812, 2408, 510, 4973, 4381, 3207, 255, 1243, 3170, 3627, 4968, 4901, 4862, 4026, 918, 4221, 4396, 2938, 2155, 1690, 3305, 4932, 879, 4610, 4180, 2676, 31, 1410, 1761, 2935, 1050, 3825, 4866, 3261, 4933, 4492, 4249, 153, 1797, 2133, 3544, 3662, 62, 4716, 2507, 2537, 2640, 748, 2713, 4586, 3076, 489, 3383, 3507, 360, 3275, 3212, 4491, 4830, 4272, 1798, 666, 2409, 3883, 4951, 4247, 4856, 371, 4875, 10, 2366, 2910, 3336, 929, 593, 3243, 3684, 4749, 1375, 150, 2970, 2363, 3472, 2571, 4187, 4008, 271, 1393, 1903, 2721, 4728, 3025, 2709, 1009, 213, 4453, 3129, 4796, 4264, 1098, 2755, 4398, 1502, 4600, 4040, 4735, 2127, 4664, 3785, 526, 4751, 2266, 489, 4832, 769, 2943, 4136, 2748, 335, 3594, 4747, 4121, 4913, 4068, 3493, 2820, 3185, 2316, 4221, 3661, 4323, 4540, 973, 1109, 1870, 3687, 551, 2815, 2429, 1334, 342, 2946, 66, 1180, 3260, 250, 2681, 181, 1801, 2082, 73, 432, 2149, 3590, 4617, 3906, 199, 4233, 4029, 2136, 1603, 2742, 2111, 1869, 3354, 4973, 3182, 3993, 702, 4615, 686, 2491, 1428, 605, 4960, 1524, 3409, 2883, 15, 296, 1767, 2236, 3172, 4513, 4879, 2071, 4662, 2816, 4854, 3350, 2844, 4837, 1359, 567, 1177, 192, 1042, 3845, 1449, 497, 303, 426, 2430, 1775, 3578, 546, 1713, 3904, 2404, 1076, 1516, 3170, 890, 3428, 1696, 4748, 1702, 2168, 959, 2900, 2889, 3713, 2404, 3478, 3775, 910, 4877, 2731, 1024, 2456, 3768, 3137, 1475, 138, 4264, 3738, 2953, 1915, 4287, 4972, 4413, 2122, 537, 3767, 4326, 3897, 415, 4717, 4001, 4698, 0, 4346, 4812, 3310, 1935, 1825, 1330, 3625, 3470, 4722, 780, 3921, 3109, 3222, 3628, 4028, 3519, 1959, 401, 221, 4062, 429, 2099, 2231, 2702, 2590, 2444, 4481, 1680, 1811, 4379, 1378, 3204, 1204, 1011, 2996, 4644, 1490, 2566, 2982, 1780, 364, 2945, 946, 532, 1610, 3808, 1008, 4309, 3406, 3408, 4750, 92, 2866, 3199, 1712, 2988, 1200, 4883, 2451, 4300, 1336, 209, 804, 2866, 4324, 4252, 2859, 4592, 547, 4306, 4270, 4109, 3693, 1630, 2550, 958, 13, 3054, 4766, 275, 3462, 4868, 3743, 679, 2305, 4217, 2066, 1746, 1319, 3122, 844, 1003, 167, 2129, 1610, 4556, 4883, 4719, 1326, 3559, 3995, 889, 702, 4434, 2359, 633, 4596, 2075, 168, 2683, 2688, 4708, 3184, 2830, 426, 2315, 2892, 4490, 1839, 3436, 1771, 276, 1290, 1721, 260, 13, 3427, 3078, 3501, 388, 4441, 1212, 1386, 1073, 1051, 1032, 4157, 2461, 2713, 4093, 4247, 198, 3181, 4869, 503, 2909, 2966, 2686, 4079, 2190, 3324, 2043, 3427, 4455, 1862, 3215, 805, 2834, 2931, 800, 803, 2611, 298, 4676, 1121, 4269, 2668, 1701, 1438, 280, 1260, 3654, 868, 1413, 4735, 4993, 4049, 2343, 3716, 1937, 4422, 192, 1381, 2338, 1620, 2820, 2281, 14, 3709, 2445, 3866, 1213, 282, 4643, 2428, 1323, 1629, 4230, 3390, 4476, 264, 3079, 4431, 2140, 1399, 1217, 4026, 4663, 2050, 1935, 1163, 1036, 4598, 3321, 1066, 1819, 1956, 1722, 2660, 4337, 3163, 895, 4713, 1073, 2890, 3828, 4515, 1370, 1950, 955, 4501, 4086, 4523, 4645, 3606, 925, 1674, 327, 4120, 3150, 3047, 1783, 166, 4313, 4753, 579, 3397, 556, 1038, 1788, 1649, 2384, 1722, 3722, 1291, 1714, 2389, 1069, 117, 2103, 2570, 1577, 3538, 357, 2802, 524, 2096, 584, 4330, 3327, 2662, 4629, 389, 2301, 2974, 3157, 2176, 3362, 3290, 3686, 3648, 744, 1644, 3168, 3300, 761, 2365, 1159]
print("unsorted: ")
print(owo)
sort(owo)
print("sorted: ")
print(owo)