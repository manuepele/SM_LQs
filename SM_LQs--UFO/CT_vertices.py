# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 11.0.0 for Linux x86 (64-bit) (July 28, 2016)
# Date: Fri 8 Jul 2022 18:47:11


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_448_403,(0,0,1):C.R2GC_448_404,(0,1,0):C.R2GC_451_405,(0,1,1):C.R2GC_451_406,(0,2,0):C.R2GC_451_405,(0,2,1):C.R2GC_451_406,(0,3,0):C.R2GC_448_403,(0,3,1):C.R2GC_448_404,(0,4,0):C.R2GC_448_403,(0,4,1):C.R2GC_448_404,(0,5,0):C.R2GC_451_405,(0,5,1):C.R2GC_451_406})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_250_27,(2,0,1):C.R2GC_250_28,(0,0,0):C.R2GC_250_27,(0,0,1):C.R2GC_250_28,(4,0,0):C.R2GC_254_35,(4,0,1):C.R2GC_254_36,(3,0,0):C.R2GC_254_35,(3,0,1):C.R2GC_254_36,(8,0,0):C.R2GC_251_29,(8,0,1):C.R2GC_251_30,(7,0,0):C.R2GC_253_33,(7,0,1):C.R2GC_459_413,(6,0,0):C.R2GC_252_31,(6,0,1):C.R2GC_458_412,(5,0,0):C.R2GC_254_35,(5,0,1):C.R2GC_254_36,(1,0,0):C.R2GC_254_35,(1,0,1):C.R2GC_254_36,(11,0,0):C.R2GC_249_25,(11,0,1):C.R2GC_249_26,(10,0,0):C.R2GC_249_25,(10,0,1):C.R2GC_249_26,(9,0,1):C.R2GC_242_3,(2,1,0):C.R2GC_250_27,(2,1,1):C.R2GC_250_28,(0,1,0):C.R2GC_250_27,(0,1,1):C.R2GC_250_28,(6,1,0):C.R2GC_455_408,(6,1,1):C.R2GC_455_409,(4,1,0):C.R2GC_254_35,(4,1,1):C.R2GC_254_36,(3,1,0):C.R2GC_254_35,(3,1,1):C.R2GC_254_36,(8,1,0):C.R2GC_251_29,(8,1,1):C.R2GC_457_411,(7,1,0):C.R2GC_253_33,(7,1,1):C.R2GC_253_34,(5,1,0):C.R2GC_254_35,(5,1,1):C.R2GC_254_36,(1,1,0):C.R2GC_254_35,(1,1,1):C.R2GC_254_36,(11,1,0):C.R2GC_249_25,(11,1,1):C.R2GC_249_26,(10,1,0):C.R2GC_249_25,(10,1,1):C.R2GC_249_26,(9,1,1):C.R2GC_242_3,(2,2,0):C.R2GC_250_27,(2,2,1):C.R2GC_250_28,(0,2,0):C.R2GC_250_27,(0,2,1):C.R2GC_250_28,(4,2,0):C.R2GC_254_35,(4,2,1):C.R2GC_254_36,(3,2,0):C.R2GC_254_35,(3,2,1):C.R2GC_254_36,(8,2,0):C.R2GC_251_29,(8,2,1):C.R2GC_454_407,(6,2,0):C.R2GC_252_31,(6,2,1):C.R2GC_252_32,(7,2,0):C.R2GC_456_410,(7,2,1):C.R2GC_250_28,(5,2,0):C.R2GC_254_35,(5,2,1):C.R2GC_254_36,(1,2,0):C.R2GC_254_35,(1,2,1):C.R2GC_254_36,(11,2,0):C.R2GC_249_25,(11,2,1):C.R2GC_249_26,(10,2,0):C.R2GC_249_25,(10,2,1):C.R2GC_249_26,(9,2,1):C.R2GC_242_3})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_423_382,(0,1,0):C.R2GC_424_383})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.c__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_394_363,(0,1,0):C.R2GC_393_362})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_440_394,(0,1,0):C.R2GC_441_395})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_410_374,(0,1,0):C.R2GC_409_373})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.u__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.g, P.s, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_443_397,(0,1,0):C.R2GC_444_398})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_372_349})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_390_359})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_406_370})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_371_348})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_389_358})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_405_369})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_388_357,(0,1,0):C.R2GC_391_360})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_404_368,(0,1,0):C.R2GC_407_371})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_421_380,(0,1,0):C.R2GC_418_377})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_437_391,(0,1,0):C.R2GC_433_387})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_438_392,(0,1,0):C.R2GC_434_388})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_379_353})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_419_378})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_435_389})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_380_354})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_420_379})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_436_390})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.a, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_471_433})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.g, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_475_435})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.W__minus__, P.Xd1__tilde__, P.Xu1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_509_479})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.W__minus__, P.Xd1__tilde__, P.Xu2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_505_473})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.a, P.a, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_473_434})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.a, P.g, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_477_436})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.G0, P.G0, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_481_439})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.G__minus__, P.G__plus__, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_481_439})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.H, P.H, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_481_439})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.H, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ] ],
                couplings = {(0,0,0):C.R2GC_530_502})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.g, P.g, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.Xd1] ] ],
                couplings = {(2,0,0):C.R2GC_479_437,(2,0,1):C.R2GC_479_438,(1,0,0):C.R2GC_479_437,(1,0,1):C.R2GC_479_438,(0,0,0):C.R2GC_264_50,(0,0,1):C.R2GC_264_51})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.W__plus__, P.Xd1, P.Xu1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_508_478})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.W__plus__, P.Xd1, P.Xu2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_504_472})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.Xd1__tilde__, P.Xd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_494_454,(0,0,1):C.R2GC_494_455,(0,0,2):C.R2GC_494_456})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.a, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_471_433})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.G0, P.G0, P.Xd1, P.Xd2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_470_432})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.G__minus__, P.G__plus__, P.Xd1, P.Xd2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_470_432})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.H, P.H, P.Xd1, P.Xd2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_470_432})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.H, P.Xd1, P.Xd2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_529_501})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.G0, P.Xd1, P.Xd2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_484_442})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_475_435})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.W__minus__, P.Xd2__tilde__, P.Xu1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_501_467})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.W__minus__, P.Xd2__tilde__, P.Xu2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_497_461})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.Xd1, P.Xd2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_495_457,(0,0,1):C.R2GC_495_458,(0,0,2):C.R2GC_495_459})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.a, P.a, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_473_434})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.a, P.g, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_477_436})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.G0, P.G0, P.Xd1__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_470_432})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.G__minus__, P.G__plus__, P.Xd1__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_470_432})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.H, P.H, P.Xd1__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_470_432})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.H, P.Xd1__tilde__, P.Xd2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_529_501})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.G0, P.G0, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_482_440})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.G__minus__, P.G__plus__, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_482_440})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.H, P.H, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_482_440})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.H, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_531_503})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.G0, P.Xd1__tilde__, P.Xd2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                couplings = {(0,0,0):C.R2GC_483_441})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.Xd2] ] ],
                couplings = {(2,0,0):C.R2GC_479_437,(2,0,1):C.R2GC_479_438,(1,0,0):C.R2GC_479_437,(1,0,1):C.R2GC_479_438,(0,0,0):C.R2GC_264_50,(0,0,1):C.R2GC_264_51})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.W__plus__, P.Xd2, P.Xu1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_500_466})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.W__plus__, P.Xd2, P.Xu2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_496_460})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.Xd1__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_495_457,(0,0,1):C.R2GC_495_458,(0,0,2):C.R2GC_495_459})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.Xd2__tilde__, P.Xd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_493_451,(0,0,1):C.R2GC_493_452,(0,0,2):C.R2GC_493_453})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.a, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_282_56})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.G__plus__, P.Xd1, P.Xu1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_486_444})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.G__plus__, P.Xd2, P.Xu1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_489_447})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.g, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_284_58})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.g, P.W__plus__, P.Xd1, P.Xu1__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_511_481,(0,0,2):C.R2GC_511_482,(0,0,1):C.R2GC_511_483})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.g, P.W__plus__, P.Xd2, P.Xu1__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_503_469,(0,0,2):C.R2GC_503_470,(0,0,1):C.R2GC_503_471})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.Xd1, P.Xu1__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_510_480})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.Xd2, P.Xu1__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_502_468})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.a, P.a, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_283_57})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.a, P.g, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_285_59})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.G0, P.G0, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_287_62})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.G__minus__, P.G__plus__, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_287_62})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.H, P.H, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_287_62})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.H, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_462_416})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.G__minus__, P.Xd1__tilde__, P.Xu1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_485_443})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.G__minus__, P.Xd2__tilde__, P.Xu1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_490_448})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.g, P.g, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.Xu1] ] ],
                couplings = {(2,0,0):C.R2GC_286_60,(2,0,1):C.R2GC_286_61,(1,0,0):C.R2GC_286_60,(1,0,1):C.R2GC_286_61,(0,0,0):C.R2GC_276_53,(0,0,1):C.R2GC_276_54})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.g, P.W__minus__, P.Xd1__tilde__, P.Xu1 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_511_481,(0,0,2):C.R2GC_511_482,(0,0,1):C.R2GC_511_483})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.g, P.W__minus__, P.Xd2__tilde__, P.Xu1 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_503_469,(0,0,2):C.R2GC_503_470,(0,0,1):C.R2GC_503_471})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.Xd1__tilde__, P.Xu1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_510_480})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.Xd2__tilde__, P.Xu1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu1] ] ],
                couplings = {(0,0,0):C.R2GC_502_468})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.Xu1__tilde__, P.Xu1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ] ],
                couplings = {(0,0,2):C.R2GC_319_82,(0,0,0):C.R2GC_319_83,(0,0,1):C.R2GC_319_84})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.a, P.Xu2__tilde__, P.Xu2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_282_56})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.G0, P.G0, P.Xu1, P.Xu2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_320_85})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.G__minus__, P.G__plus__, P.Xu1, P.Xu2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_320_85})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.H, P.H, P.Xu1, P.Xu2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_320_85})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.H, P.Xu1, P.Xu2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_464_418})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.G0, P.Xu1, P.Xu2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_463_417})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.G__plus__, P.Xd1, P.Xu2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_492_450})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.G__plus__, P.Xd2, P.Xu2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_488_446})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.g, P.Xu2__tilde__, P.Xu2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_284_58})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.W__plus__, P.Xd1, P.Xu2__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_507_475,(0,0,2):C.R2GC_507_476,(0,0,1):C.R2GC_507_477})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.g, P.W__plus__, P.Xd2, P.Xu2__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_499_463,(0,0,2):C.R2GC_499_464,(0,0,1):C.R2GC_499_465})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.Xd1, P.Xu2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd1, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_506_474})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.Xd2, P.Xu2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.Xd2, P.Xu2] ] ],
                couplings = {(0,0,0):C.R2GC_498_462})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,2):C.R2GC_334_111,(0,0,0):C.R2GC_334_112,(0,0,1):C.R2GC_334_113})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.a, P.a, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_283_57})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.a, P.g, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_285_59})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.G0, P.G0, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_320_85})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.G__minus__, P.G__plus__, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_320_85})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.H, P.H, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_320_85})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.H, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_464_418})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.G0, P.G0, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_303_67})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.G__minus__, P.G__plus__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_303_67})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.H, P.H, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_303_67})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.H, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_461_415})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.G__minus__, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_491_449})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.G__minus__, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd2, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_487_445})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.G0, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_465_419})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(2,0,0):C.R2GC_286_60,(2,0,1):C.R2GC_286_61,(1,0,0):C.R2GC_286_60,(1,0,1):C.R2GC_286_61,(0,0,0):C.R2GC_276_53,(0,0,1):C.R2GC_276_54})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_507_475,(0,0,2):C.R2GC_507_476,(0,0,1):C.R2GC_507_477})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_499_463,(0,0,2):C.R2GC_499_464,(0,0,1):C.R2GC_499_465})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_506_474})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd2, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_498_462})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,2):C.R2GC_334_111,(0,0,0):C.R2GC_334_112,(0,0,1):C.R2GC_334_113})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,2):C.R2GC_318_79,(0,0,0):C.R2GC_318_80,(0,0,1):C.R2GC_318_81})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ] ],
                 couplings = {(0,0,0):C.R2GC_518_489,(0,1,0):C.R2GC_519_490})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_512_484,(0,1,0):C.R2GC_514_485})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_514_485,(0,1,0):C.R2GC_512_484})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ] ],
                 couplings = {(0,0,0):C.R2GC_522_493})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ] ],
                 couplings = {(0,0,0):C.R2GC_524_495})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_521_492,(0,1,0):C.R2GC_520_491})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_516_486})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1], [P.g, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_517_487,(0,0,1):C.R2GC_517_488})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_516_486})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1], [P.g, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_517_487,(0,0,1):C.R2GC_517_488})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_523_494})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_525_496})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_527_498,(0,0,1):C.R2GC_527_499})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_526_497})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_526_497})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ] ],
                 couplings = {(0,0,1):C.R2GC_528_500,(0,0,0):C.R2GC_527_499})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.R2GC_288_63,(0,1,0):C.R2GC_289_64})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_323_87,(0,1,0):C.R2GC_321_86})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_321_86,(0,1,0):C.R2GC_323_87})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.R2GC_290_65})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.R2GC_291_66})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_304_68,(0,1,0):C.R2GC_305_69})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_325_88})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1], [P.g, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_326_89,(0,0,1):C.R2GC_326_90})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_325_88})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1], [P.g, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_326_89,(0,0,1):C.R2GC_326_90})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_306_70})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_307_71})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_327_91,(0,0,1):C.R2GC_327_92})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_329_94})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_329_94})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,1):C.R2GC_328_93,(0,0,0):C.R2GC_327_92})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.Xd1, P.Xu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,1):C.R2GC_469_429,(0,0,0):C.R2GC_469_430,(0,0,2):C.R2GC_469_431})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.Xd2, P.Xu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,1):C.R2GC_467_423,(0,0,0):C.R2GC_467_424,(0,0,2):C.R2GC_467_425})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.Xd1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,1):C.R2GC_469_429,(0,0,0):C.R2GC_469_430,(0,0,2):C.R2GC_469_431})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.Xd2__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ] ],
                 couplings = {(0,0,1):C.R2GC_467_423,(0,0,0):C.R2GC_467_424,(0,0,2):C.R2GC_467_425})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.Xd1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ] ],
                 couplings = {(0,0,2):C.R2GC_468_426,(0,0,0):C.R2GC_468_427,(0,0,1):C.R2GC_468_428})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.Xd2, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2] ] ],
                 couplings = {(0,0,2):C.R2GC_466_420,(0,0,0):C.R2GC_466_421,(0,0,1):C.R2GC_466_422})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ] ],
                 couplings = {(0,0,2):C.R2GC_468_426,(0,0,0):C.R2GC_468_427,(0,0,1):C.R2GC_468_428})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2] ] ],
                 couplings = {(0,0,2):C.R2GC_466_420,(0,0,0):C.R2GC_466_421,(0,0,1):C.R2GC_466_422})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_260_49})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_260_49})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_260_49})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_258_47})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_258_47})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_258_47})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_259_48})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_259_48})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_259_48})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_259_48})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_259_48})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_259_48})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_385_356})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_401_367})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_415_376})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_429_385})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_430_386})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_422_381})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_392_361})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_439_393})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_408_372})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_442_396})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_377_351,(0,1,0):C.R2GC_378_352})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_377_351,(0,1,0):C.R2GC_378_352})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_377_351,(0,1,0):C.R2GC_378_352})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_369_346,(0,1,0):C.R2GC_370_347})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_369_346,(0,1,0):C.R2GC_370_347})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_369_346,(0,1,0):C.R2GC_370_347})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_368_345,(0,2,0):C.R2GC_368_345,(0,1,0):C.R2GC_365_344,(0,3,0):C.R2GC_365_344})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_376_350,(0,2,0):C.R2GC_376_350,(0,1,0):C.R2GC_365_344,(0,3,0):C.R2GC_365_344})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_384_355,(0,2,0):C.R2GC_384_355,(0,1,0):C.R2GC_365_344,(0,3,0):C.R2GC_365_344})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_400_366,(0,2,0):C.R2GC_400_366,(0,1,0):C.R2GC_365_344,(0,3,0):C.R2GC_365_344})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_414_375,(0,2,0):C.R2GC_414_375,(0,1,0):C.R2GC_365_344,(0,3,0):C.R2GC_365_344})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_428_384,(0,2,0):C.R2GC_428_384,(0,1,0):C.R2GC_365_344,(0,3,0):C.R2GC_365_344})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xd1] ] ],
                 couplings = {(0,0,0):C.R2GC_395_364,(0,1,0):C.R2GC_269_52})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.R2GC_445_399,(0,1,0):C.R2GC_281_55})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xd2] ] ],
                 couplings = {(0,0,0):C.R2GC_396_365,(0,1,0):C.R2GC_269_52})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.R2GC_460_414,(0,1,0):C.R2GC_281_55})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,4):C.R2GC_447_402,(0,1,0):C.R2GC_243_4,(0,1,2):C.R2GC_243_5,(0,1,3):C.R2GC_243_6,(0,1,5):C.R2GC_243_7,(0,1,6):C.R2GC_243_8,(0,1,7):C.R2GC_243_9,(0,2,1):C.R2GC_446_400,(0,2,4):C.R2GC_446_401})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_257_41,(0,0,1):C.R2GC_257_42,(0,0,2):C.R2GC_257_43,(0,0,3):C.R2GC_257_44,(0,0,4):C.R2GC_257_45,(0,0,5):C.R2GC_257_46})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_247_21,(0,0,1):C.R2GC_247_22,(0,1,0):C.R2GC_247_21,(0,1,1):C.R2GC_247_22,(0,2,0):C.R2GC_247_21,(0,2,1):C.R2GC_247_22})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_255_37,(0,0,1):C.R2GC_255_38,(0,1,0):C.R2GC_255_37,(0,1,1):C.R2GC_255_38,(0,2,0):C.R2GC_255_37,(0,2,1):C.R2GC_255_38})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_316_77,(0,0,1):C.R2GC_316_78,(0,1,0):C.R2GC_316_77,(0,1,1):C.R2GC_316_78,(0,2,0):C.R2GC_316_77,(0,2,1):C.R2GC_316_78})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_314_72,(0,0,1):C.R2GC_314_73,(0,0,2):C.R2GC_314_74,(0,0,3):C.R2GC_314_75,(0,0,4):C.R2GC_314_76,(0,1,0):C.R2GC_314_72,(0,1,1):C.R2GC_314_73,(0,1,2):C.R2GC_314_74,(0,1,3):C.R2GC_314_75,(0,1,4):C.R2GC_314_76,(0,2,0):C.R2GC_314_72,(0,2,1):C.R2GC_314_73,(0,2,2):C.R2GC_314_74,(0,2,3):C.R2GC_314_75,(0,2,4):C.R2GC_314_76})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_248_23,(0,0,1):C.R2GC_248_24,(0,1,0):C.R2GC_248_23,(0,1,1):C.R2GC_248_24,(0,2,0):C.R2GC_248_23,(0,2,1):C.R2GC_248_24})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,0,0):C.R2GC_240_1,(1,0,1):C.R2GC_240_2,(0,1,0):C.R2GC_256_39,(0,1,1):C.R2GC_256_40,(0,2,0):C.R2GC_256_39,(0,2,1):C.R2GC_256_40,(0,3,0):C.R2GC_256_39,(0,3,1):C.R2GC_256_40})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_245_10,(0,0,1):C.R2GC_245_11,(0,0,2):C.R2GC_245_12,(0,0,3):C.R2GC_245_13,(0,0,4):C.R2GC_245_14,(0,0,5):C.R2GC_245_15})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_245_10,(0,0,1):C.R2GC_245_11,(0,0,2):C.R2GC_245_12,(0,0,3):C.R2GC_245_13,(0,0,4):C.R2GC_245_14,(0,0,5):C.R2GC_245_15})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_246_16,(0,0,1):C.R2GC_246_17,(0,0,2):C.R2GC_246_18,(0,0,3):C.R2GC_246_19,(0,0,4):C.R2GC_246_20})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1__tilde__, P.Xd1, P.Xd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1] ], [ [P.g] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_330_95,(1,0,0):C.R2GC_330_96,(1,0,3):C.R2GC_330_97,(1,0,5):C.R2GC_330_98,(1,0,1):C.R2GC_330_99,(1,0,4):C.R2GC_330_100,(0,0,2):C.R2GC_330_95,(0,0,0):C.R2GC_330_96,(0,0,3):C.R2GC_330_97,(0,0,5):C.R2GC_330_98,(0,0,1):C.R2GC_330_99,(0,0,4):C.R2GC_330_100})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1] ], [ [P.a, P.g, P.Xd1, P.Xu1] ], [ [P.a, P.g, P.Xu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.R2GC_341_159,(1,0,0):C.R2GC_341_160,(1,0,5):C.R2GC_341_161,(1,0,9):C.R2GC_341_162,(1,0,13):C.R2GC_341_163,(1,0,15):C.R2GC_341_164,(1,0,1):C.R2GC_341_165,(1,0,3):C.R2GC_341_166,(1,0,6):C.R2GC_341_167,(1,0,8):C.R2GC_341_168,(1,0,10):C.R2GC_341_169,(1,0,12):C.R2GC_341_170,(1,0,14):C.R2GC_341_171,(1,0,2):C.R2GC_341_172,(1,0,7):C.R2GC_341_173,(1,0,11):C.R2GC_341_174,(0,0,4):C.R2GC_340_143,(0,0,0):C.R2GC_340_144,(0,0,5):C.R2GC_340_145,(0,0,9):C.R2GC_340_146,(0,0,13):C.R2GC_340_147,(0,0,15):C.R2GC_340_148,(0,0,1):C.R2GC_340_149,(0,0,3):C.R2GC_340_150,(0,0,6):C.R2GC_340_151,(0,0,8):C.R2GC_340_152,(0,0,10):C.R2GC_340_153,(0,0,12):C.R2GC_340_154,(0,0,14):C.R2GC_340_155,(0,0,2):C.R2GC_340_156,(0,0,7):C.R2GC_340_157,(0,0,11):C.R2GC_340_158})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.Xu1__tilde__, P.Xu1__tilde__, P.Xu1, P.Xu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xu1] ], [ [P.g] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_332_103,(1,0,0):C.R2GC_332_104,(1,0,3):C.R2GC_332_105,(1,0,5):C.R2GC_332_106,(1,0,1):C.R2GC_332_107,(1,0,4):C.R2GC_332_108,(0,0,2):C.R2GC_332_103,(0,0,0):C.R2GC_332_104,(0,0,3):C.R2GC_332_105,(0,0,5):C.R2GC_332_106,(0,0,1):C.R2GC_332_107,(0,0,4):C.R2GC_332_108})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1__tilde__, P.Xd1, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_336_117,(1,0,1):C.R2GC_336_118,(1,0,2):C.R2GC_336_119,(1,0,0):C.R2GC_336_120,(0,0,3):C.R2GC_336_117,(0,0,1):C.R2GC_336_118,(0,0,2):C.R2GC_336_119,(0,0,0):C.R2GC_336_120})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu1, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_357_290,(1,0,8):C.R2GC_357_291,(1,0,1):C.R2GC_357_292,(1,0,4):C.R2GC_357_293,(1,0,6):C.R2GC_357_294,(1,0,7):C.R2GC_357_295,(1,0,2):C.R2GC_357_296,(1,0,3):C.R2GC_357_297,(1,0,5):C.R2GC_357_298,(0,0,0):C.R2GC_356_281,(0,0,8):C.R2GC_356_282,(0,0,1):C.R2GC_356_283,(0,0,4):C.R2GC_356_284,(0,0,6):C.R2GC_356_285,(0,0,7):C.R2GC_356_286,(0,0,2):C.R2GC_356_287,(0,0,3):C.R2GC_356_288,(0,0,5):C.R2GC_356_289})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1__tilde__, P.Xd2, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_335_114,(1,0,1):C.R2GC_335_115,(1,0,0):C.R2GC_335_116,(0,0,2):C.R2GC_335_114,(0,0,1):C.R2GC_335_115,(0,0,0):C.R2GC_335_116})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_336_117,(1,0,1):C.R2GC_336_118,(1,0,2):C.R2GC_336_119,(1,0,0):C.R2GC_336_120,(0,0,3):C.R2GC_336_117,(0,0,1):C.R2GC_336_118,(0,0,2):C.R2GC_336_119,(0,0,0):C.R2GC_336_120})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu1, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_357_290,(1,0,8):C.R2GC_357_291,(1,0,1):C.R2GC_357_292,(1,0,4):C.R2GC_357_293,(1,0,6):C.R2GC_357_294,(1,0,7):C.R2GC_357_295,(1,0,2):C.R2GC_357_296,(1,0,3):C.R2GC_357_297,(1,0,5):C.R2GC_357_298,(0,0,0):C.R2GC_356_281,(0,0,8):C.R2GC_356_282,(0,0,1):C.R2GC_356_283,(0,0,4):C.R2GC_356_284,(0,0,6):C.R2GC_356_285,(0,0,7):C.R2GC_356_286,(0,0,2):C.R2GC_356_287,(0,0,3):C.R2GC_356_288,(0,0,5):C.R2GC_356_289})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1], [P.a, P.g, P.Xd2] ], [ [P.a, P.g, P.Xd1, P.Xd2] ], [ [P.g] ], [ [P.g, P.Xd1], [P.g, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_339_134,(1,0,0):C.R2GC_339_135,(1,0,4):C.R2GC_339_136,(1,0,8):C.R2GC_339_137,(1,0,1):C.R2GC_339_138,(1,0,5):C.R2GC_339_139,(1,0,7):C.R2GC_339_140,(1,0,2):C.R2GC_339_141,(1,0,6):C.R2GC_339_142,(0,0,3):C.R2GC_338_125,(0,0,0):C.R2GC_338_126,(0,0,4):C.R2GC_338_127,(0,0,8):C.R2GC_338_128,(0,0,1):C.R2GC_338_129,(0,0,5):C.R2GC_338_130,(0,0,7):C.R2GC_338_131,(0,0,2):C.R2GC_338_132,(0,0,6):C.R2GC_338_133})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd2] ], [ [P.a, P.g, P.Xd2, P.Xu1] ], [ [P.a, P.g, P.Xu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.R2GC_341_159,(1,0,0):C.R2GC_341_160,(1,0,5):C.R2GC_359_307,(1,0,9):C.R2GC_341_162,(1,0,13):C.R2GC_341_163,(1,0,15):C.R2GC_359_308,(1,0,1):C.R2GC_341_165,(1,0,3):C.R2GC_341_166,(1,0,6):C.R2GC_359_309,(1,0,8):C.R2GC_359_310,(1,0,10):C.R2GC_341_169,(1,0,12):C.R2GC_359_311,(1,0,14):C.R2GC_359_312,(1,0,2):C.R2GC_341_172,(1,0,7):C.R2GC_359_313,(1,0,11):C.R2GC_359_314,(0,0,4):C.R2GC_340_143,(0,0,0):C.R2GC_340_144,(0,0,5):C.R2GC_358_299,(0,0,9):C.R2GC_340_146,(0,0,13):C.R2GC_340_147,(0,0,15):C.R2GC_358_300,(0,0,1):C.R2GC_340_149,(0,0,3):C.R2GC_340_150,(0,0,6):C.R2GC_358_301,(0,0,8):C.R2GC_358_302,(0,0,10):C.R2GC_340_153,(0,0,12):C.R2GC_358_303,(0,0,14):C.R2GC_358_304,(0,0,2):C.R2GC_340_156,(0,0,7):C.R2GC_358_305,(0,0,11):C.R2GC_358_306})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd2__tilde__, P.Xd2, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_337_121,(1,0,1):C.R2GC_337_122,(1,0,2):C.R2GC_337_123,(1,0,0):C.R2GC_337_124,(0,0,3):C.R2GC_337_121,(0,0,1):C.R2GC_337_122,(0,0,2):C.R2GC_337_123,(0,0,0):C.R2GC_337_124})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.Xd1, P.Xd1, P.Xd2__tilde__, P.Xd2__tilde__ ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_335_114,(1,0,1):C.R2GC_335_115,(1,0,0):C.R2GC_335_116,(0,0,2):C.R2GC_335_114,(0,0,1):C.R2GC_335_115,(0,0,0):C.R2GC_335_116})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_337_121,(1,0,1):C.R2GC_337_122,(1,0,2):C.R2GC_337_123,(1,0,0):C.R2GC_337_124,(0,0,3):C.R2GC_337_121,(0,0,1):C.R2GC_337_122,(0,0,2):C.R2GC_337_123,(0,0,0):C.R2GC_337_124})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.Xd2__tilde__, P.Xd2__tilde__, P.Xd2, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd2] ], [ [P.g] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_330_95,(1,0,0):C.R2GC_330_96,(1,0,3):C.R2GC_330_97,(1,0,5):C.R2GC_331_101,(1,0,1):C.R2GC_330_99,(1,0,4):C.R2GC_331_102,(0,0,2):C.R2GC_330_95,(0,0,0):C.R2GC_330_96,(0,0,3):C.R2GC_330_97,(0,0,5):C.R2GC_331_101,(0,0,1):C.R2GC_330_99,(0,0,4):C.R2GC_331_102})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd1, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_343_184,(1,0,8):C.R2GC_343_185,(1,0,1):C.R2GC_343_186,(1,0,3):C.R2GC_343_187,(1,0,6):C.R2GC_343_188,(1,0,7):C.R2GC_343_189,(1,0,2):C.R2GC_343_190,(1,0,4):C.R2GC_343_191,(1,0,5):C.R2GC_343_192,(0,0,0):C.R2GC_342_175,(0,0,8):C.R2GC_342_176,(0,0,1):C.R2GC_342_177,(0,0,3):C.R2GC_342_178,(0,0,6):C.R2GC_342_179,(0,0,7):C.R2GC_342_180,(0,0,2):C.R2GC_342_181,(0,0,4):C.R2GC_342_182,(0,0,5):C.R2GC_342_183})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.Xu1__tilde__, P.Xu1__tilde__, P.Xu1, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_361_318,(1,0,1):C.R2GC_361_319,(1,0,2):C.R2GC_361_320,(1,0,0):C.R2GC_361_321,(0,0,3):C.R2GC_361_318,(0,0,1):C.R2GC_361_319,(0,0,2):C.R2GC_361_320,(0,0,0):C.R2GC_361_321})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_352_253,(1,0,9):C.R2GC_352_254,(1,0,1):C.R2GC_352_255,(1,0,4):C.R2GC_352_256,(1,0,7):C.R2GC_352_257,(1,0,8):C.R2GC_352_258,(1,0,2):C.R2GC_352_259,(1,0,3):C.R2GC_352_260,(1,0,5):C.R2GC_352_261,(1,0,6):C.R2GC_352_262,(0,0,0):C.R2GC_350_243,(0,0,9):C.R2GC_350_244,(0,0,1):C.R2GC_350_245,(0,0,4):C.R2GC_350_246,(0,0,7):C.R2GC_350_247,(0,0,8):C.R2GC_350_248,(0,0,2):C.R2GC_350_249,(0,0,3):C.R2GC_350_250,(0,0,5):C.R2GC_350_251,(0,0,6):C.R2GC_350_252})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_352_253,(1,0,9):C.R2GC_352_254,(1,0,1):C.R2GC_352_255,(1,0,4):C.R2GC_352_256,(1,0,7):C.R2GC_352_257,(1,0,8):C.R2GC_352_258,(1,0,2):C.R2GC_352_259,(1,0,3):C.R2GC_352_260,(1,0,5):C.R2GC_352_261,(1,0,6):C.R2GC_352_262,(0,0,0):C.R2GC_350_243,(0,0,9):C.R2GC_350_244,(0,0,1):C.R2GC_350_245,(0,0,4):C.R2GC_350_246,(0,0,7):C.R2GC_350_247,(0,0,8):C.R2GC_350_248,(0,0,2):C.R2GC_350_249,(0,0,3):C.R2GC_350_250,(0,0,5):C.R2GC_350_251,(0,0,6):C.R2GC_350_252})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_355_272,(1,0,8):C.R2GC_355_273,(1,0,1):C.R2GC_355_274,(1,0,3):C.R2GC_355_275,(1,0,6):C.R2GC_355_276,(1,0,7):C.R2GC_355_277,(1,0,2):C.R2GC_355_278,(1,0,4):C.R2GC_355_279,(1,0,5):C.R2GC_355_280,(0,0,0):C.R2GC_354_263,(0,0,8):C.R2GC_354_264,(0,0,1):C.R2GC_354_265,(0,0,3):C.R2GC_354_266,(0,0,6):C.R2GC_354_267,(0,0,7):C.R2GC_354_268,(0,0,2):C.R2GC_354_269,(0,0,4):C.R2GC_354_270,(0,0,5):C.R2GC_354_271})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.Xu1__tilde__, P.Xu1__tilde__, P.Xu2, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_360_315,(1,0,1):C.R2GC_360_316,(1,0,0):C.R2GC_360_317,(0,0,2):C.R2GC_360_315,(0,0,1):C.R2GC_360_316,(0,0,0):C.R2GC_360_317})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd1, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_343_184,(1,0,8):C.R2GC_343_185,(1,0,1):C.R2GC_343_186,(1,0,3):C.R2GC_343_187,(1,0,6):C.R2GC_343_188,(1,0,7):C.R2GC_343_189,(1,0,2):C.R2GC_343_190,(1,0,4):C.R2GC_343_191,(1,0,5):C.R2GC_343_192,(0,0,0):C.R2GC_342_175,(0,0,8):C.R2GC_342_176,(0,0,1):C.R2GC_342_177,(0,0,3):C.R2GC_342_178,(0,0,6):C.R2GC_342_179,(0,0,7):C.R2GC_342_180,(0,0,2):C.R2GC_342_181,(0,0,4):C.R2GC_342_182,(0,0,5):C.R2GC_342_183})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.Xu1__tilde__, P.Xu1, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_361_318,(1,0,1):C.R2GC_361_319,(1,0,2):C.R2GC_361_320,(1,0,0):C.R2GC_361_321,(0,0,3):C.R2GC_361_318,(0,0,1):C.R2GC_361_319,(0,0,2):C.R2GC_361_320,(0,0,0):C.R2GC_361_321})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_352_253,(1,0,9):C.R2GC_352_254,(1,0,1):C.R2GC_352_255,(1,0,4):C.R2GC_352_256,(1,0,7):C.R2GC_352_257,(1,0,8):C.R2GC_352_258,(1,0,2):C.R2GC_352_259,(1,0,3):C.R2GC_352_260,(1,0,5):C.R2GC_352_261,(1,0,6):C.R2GC_352_262,(0,0,0):C.R2GC_350_243,(0,0,9):C.R2GC_350_244,(0,0,1):C.R2GC_350_245,(0,0,4):C.R2GC_350_246,(0,0,7):C.R2GC_350_247,(0,0,8):C.R2GC_350_248,(0,0,2):C.R2GC_350_249,(0,0,3):C.R2GC_350_250,(0,0,5):C.R2GC_350_251,(0,0,6):C.R2GC_350_252})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_352_253,(1,0,9):C.R2GC_352_254,(1,0,1):C.R2GC_352_255,(1,0,4):C.R2GC_352_256,(1,0,7):C.R2GC_352_257,(1,0,8):C.R2GC_352_258,(1,0,2):C.R2GC_352_259,(1,0,3):C.R2GC_352_260,(1,0,5):C.R2GC_352_261,(1,0,6):C.R2GC_352_262,(0,0,0):C.R2GC_350_243,(0,0,9):C.R2GC_350_244,(0,0,1):C.R2GC_350_245,(0,0,4):C.R2GC_350_246,(0,0,7):C.R2GC_350_247,(0,0,8):C.R2GC_350_248,(0,0,2):C.R2GC_350_249,(0,0,3):C.R2GC_350_250,(0,0,5):C.R2GC_350_251,(0,0,6):C.R2GC_350_252})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_355_272,(1,0,8):C.R2GC_355_273,(1,0,1):C.R2GC_355_274,(1,0,3):C.R2GC_355_275,(1,0,6):C.R2GC_355_276,(1,0,7):C.R2GC_355_277,(1,0,2):C.R2GC_355_278,(1,0,4):C.R2GC_355_279,(1,0,5):C.R2GC_355_280,(0,0,0):C.R2GC_354_263,(0,0,8):C.R2GC_354_264,(0,0,1):C.R2GC_354_265,(0,0,3):C.R2GC_354_266,(0,0,6):C.R2GC_354_267,(0,0,7):C.R2GC_354_268,(0,0,2):C.R2GC_354_269,(0,0,4):C.R2GC_354_270,(0,0,5):C.R2GC_354_271})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1] ], [ [P.a, P.g, P.Xd1, P.Xu2] ], [ [P.a, P.g, P.Xu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu2] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.R2GC_341_159,(1,0,0):C.R2GC_341_160,(1,0,5):C.R2GC_345_201,(1,0,9):C.R2GC_341_162,(1,0,13):C.R2GC_341_163,(1,0,15):C.R2GC_345_202,(1,0,1):C.R2GC_341_165,(1,0,3):C.R2GC_341_166,(1,0,6):C.R2GC_345_203,(1,0,8):C.R2GC_345_204,(1,0,10):C.R2GC_341_169,(1,0,12):C.R2GC_345_205,(1,0,14):C.R2GC_345_206,(1,0,2):C.R2GC_341_172,(1,0,7):C.R2GC_345_207,(1,0,11):C.R2GC_345_208,(0,0,4):C.R2GC_340_143,(0,0,0):C.R2GC_340_144,(0,0,5):C.R2GC_344_193,(0,0,9):C.R2GC_340_146,(0,0,13):C.R2GC_340_147,(0,0,15):C.R2GC_344_194,(0,0,1):C.R2GC_340_149,(0,0,3):C.R2GC_340_150,(0,0,6):C.R2GC_344_195,(0,0,8):C.R2GC_344_196,(0,0,10):C.R2GC_340_153,(0,0,12):C.R2GC_344_197,(0,0,14):C.R2GC_344_198,(0,0,2):C.R2GC_340_156,(0,0,7):C.R2GC_344_199,(0,0,11):C.R2GC_344_200})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.Xu1__tilde__, P.Xu1, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xu1], [P.a, P.g, P.Xu2] ], [ [P.a, P.g, P.Xu1, P.Xu2] ], [ [P.g] ], [ [P.g, P.Xu1], [P.g, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_364_335,(1,0,0):C.R2GC_364_336,(1,0,4):C.R2GC_364_337,(1,0,8):C.R2GC_364_338,(1,0,1):C.R2GC_364_339,(1,0,5):C.R2GC_364_340,(1,0,7):C.R2GC_364_341,(1,0,2):C.R2GC_364_342,(1,0,6):C.R2GC_364_343,(0,0,3):C.R2GC_363_326,(0,0,0):C.R2GC_363_327,(0,0,4):C.R2GC_363_328,(0,0,8):C.R2GC_363_329,(0,0,1):C.R2GC_363_330,(0,0,5):C.R2GC_363_331,(0,0,7):C.R2GC_363_332,(0,0,2):C.R2GC_363_333,(0,0,6):C.R2GC_363_334})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_347_218,(1,0,8):C.R2GC_347_219,(1,0,1):C.R2GC_347_220,(1,0,4):C.R2GC_347_221,(1,0,6):C.R2GC_347_222,(1,0,7):C.R2GC_347_223,(1,0,2):C.R2GC_347_224,(1,0,3):C.R2GC_347_225,(1,0,5):C.R2GC_347_226,(0,0,0):C.R2GC_346_209,(0,0,8):C.R2GC_346_210,(0,0,1):C.R2GC_346_211,(0,0,4):C.R2GC_346_212,(0,0,6):C.R2GC_346_213,(0,0,7):C.R2GC_346_214,(0,0,2):C.R2GC_346_215,(0,0,3):C.R2GC_346_216,(0,0,5):C.R2GC_346_217})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.R2GC_347_218,(1,0,8):C.R2GC_347_219,(1,0,1):C.R2GC_347_220,(1,0,4):C.R2GC_347_221,(1,0,6):C.R2GC_347_222,(1,0,7):C.R2GC_347_223,(1,0,2):C.R2GC_347_224,(1,0,3):C.R2GC_347_225,(1,0,5):C.R2GC_347_226,(0,0,0):C.R2GC_346_209,(0,0,8):C.R2GC_346_210,(0,0,1):C.R2GC_346_211,(0,0,4):C.R2GC_346_212,(0,0,6):C.R2GC_346_213,(0,0,7):C.R2GC_346_214,(0,0,2):C.R2GC_346_215,(0,0,3):C.R2GC_346_216,(0,0,5):C.R2GC_346_217})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd2] ], [ [P.a, P.g, P.Xd2, P.Xu2] ], [ [P.a, P.g, P.Xu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu2] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.R2GC_341_159,(1,0,0):C.R2GC_341_160,(1,0,5):C.R2GC_349_235,(1,0,9):C.R2GC_341_162,(1,0,13):C.R2GC_341_163,(1,0,15):C.R2GC_349_236,(1,0,1):C.R2GC_341_165,(1,0,3):C.R2GC_341_166,(1,0,6):C.R2GC_349_237,(1,0,8):C.R2GC_349_238,(1,0,10):C.R2GC_341_169,(1,0,12):C.R2GC_349_239,(1,0,14):C.R2GC_349_240,(1,0,2):C.R2GC_341_172,(1,0,7):C.R2GC_349_241,(1,0,11):C.R2GC_349_242,(0,0,4):C.R2GC_340_143,(0,0,0):C.R2GC_340_144,(0,0,5):C.R2GC_348_227,(0,0,9):C.R2GC_340_146,(0,0,13):C.R2GC_340_147,(0,0,15):C.R2GC_348_228,(0,0,1):C.R2GC_340_149,(0,0,3):C.R2GC_340_150,(0,0,6):C.R2GC_348_229,(0,0,8):C.R2GC_348_230,(0,0,10):C.R2GC_340_153,(0,0,12):C.R2GC_348_231,(0,0,14):C.R2GC_348_232,(0,0,2):C.R2GC_340_156,(0,0,7):C.R2GC_348_233,(0,0,11):C.R2GC_348_234})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.Xu1__tilde__, P.Xu2__tilde__, P.Xu2, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_362_322,(1,0,1):C.R2GC_362_323,(1,0,2):C.R2GC_362_324,(1,0,0):C.R2GC_362_325,(0,0,3):C.R2GC_362_322,(0,0,1):C.R2GC_362_323,(0,0,2):C.R2GC_362_324,(0,0,0):C.R2GC_362_325})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.Xu1, P.Xu1, P.Xu2__tilde__, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_360_315,(1,0,1):C.R2GC_360_316,(1,0,0):C.R2GC_360_317,(0,0,2):C.R2GC_360_315,(0,0,1):C.R2GC_360_316,(0,0,0):C.R2GC_360_317})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.Xu1, P.Xu2__tilde__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_362_322,(1,0,1):C.R2GC_362_323,(1,0,2):C.R2GC_362_324,(1,0,0):C.R2GC_362_325,(0,0,3):C.R2GC_362_322,(0,0,1):C.R2GC_362_323,(0,0,2):C.R2GC_362_324,(0,0,0):C.R2GC_362_325})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.Xu2__tilde__, P.Xu2__tilde__, P.Xu2, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xu2] ], [ [P.g] ], [ [P.g, P.Xu2] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_332_103,(1,0,0):C.R2GC_332_104,(1,0,3):C.R2GC_332_105,(1,0,5):C.R2GC_333_109,(1,0,1):C.R2GC_332_107,(1,0,4):C.R2GC_333_110,(0,0,2):C.R2GC_332_103,(0,0,0):C.R2GC_332_104,(0,0,3):C.R2GC_332_105,(0,0,5):C.R2GC_333_109,(0,0,1):C.R2GC_332_107,(0,0,4):C.R2GC_333_110})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd1], [P.Xd2] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu1], [P.Xu2] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_448_664,(0,0,1):C.UVGC_448_665,(0,0,2):C.UVGC_448_666,(0,0,3):C.UVGC_448_667,(0,0,4):C.UVGC_244_10,(0,0,5):C.UVGC_448_668,(0,0,6):C.UVGC_448_669,(0,0,7):C.UVGC_448_670,(0,0,8):C.UVGC_448_671,(0,0,10):C.UVGC_448_672,(0,0,11):C.UVGC_448_673,(0,0,13):C.UVGC_448_674,(0,1,0):C.UVGC_451_683,(0,1,1):C.UVGC_451_684,(0,1,2):C.UVGC_451_685,(0,1,3):C.UVGC_452_694,(0,1,4):C.UVGC_452_695,(0,1,5):C.UVGC_451_687,(0,1,6):C.UVGC_451_688,(0,1,7):C.UVGC_451_689,(0,1,8):C.UVGC_452_696,(0,1,10):C.UVGC_452_697,(0,1,11):C.UVGC_452_698,(0,1,13):C.UVGC_452_699,(0,3,0):C.UVGC_451_683,(0,3,1):C.UVGC_451_684,(0,3,2):C.UVGC_451_685,(0,3,3):C.UVGC_451_686,(0,3,4):C.UVGC_241_2,(0,3,5):C.UVGC_451_687,(0,3,6):C.UVGC_451_688,(0,3,7):C.UVGC_451_689,(0,3,8):C.UVGC_451_690,(0,3,10):C.UVGC_451_691,(0,3,11):C.UVGC_451_692,(0,3,13):C.UVGC_451_693,(0,5,0):C.UVGC_448_664,(0,5,1):C.UVGC_448_665,(0,5,2):C.UVGC_448_666,(0,5,3):C.UVGC_450_677,(0,5,4):C.UVGC_450_678,(0,5,5):C.UVGC_448_668,(0,5,6):C.UVGC_448_669,(0,5,7):C.UVGC_448_670,(0,5,8):C.UVGC_450_679,(0,5,10):C.UVGC_450_680,(0,5,11):C.UVGC_450_681,(0,5,13):C.UVGC_450_682,(0,6,0):C.UVGC_448_664,(0,6,1):C.UVGC_448_665,(0,6,2):C.UVGC_448_666,(0,6,3):C.UVGC_449_675,(0,6,4):C.UVGC_449_676,(0,6,5):C.UVGC_448_668,(0,6,6):C.UVGC_448_669,(0,6,7):C.UVGC_448_670,(0,6,8):C.UVGC_448_671,(0,6,10):C.UVGC_448_672,(0,6,11):C.UVGC_448_673,(0,6,13):C.UVGC_448_674,(0,7,0):C.UVGC_451_683,(0,7,1):C.UVGC_451_684,(0,7,2):C.UVGC_451_685,(0,7,3):C.UVGC_453_700,(0,7,4):C.UVGC_453_701,(0,7,5):C.UVGC_451_687,(0,7,6):C.UVGC_451_688,(0,7,7):C.UVGC_451_689,(0,7,8):C.UVGC_452_696,(0,7,10):C.UVGC_452_697,(0,7,11):C.UVGC_452_698,(0,7,13):C.UVGC_452_699,(0,2,3):C.UVGC_241_1,(0,2,4):C.UVGC_241_2,(0,4,3):C.UVGC_244_9,(0,4,4):C.UVGC_244_10,(0,4,9):C.UVGC_244_11,(0,4,12):C.UVGC_244_12})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd1], [P.Xd2] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu1], [P.Xu2] ], [ [P.Xu2] ] ],
                 couplings = {(2,0,4):C.UVGC_250_25,(2,0,5):C.UVGC_250_26,(2,0,10):C.UVGC_250_27,(2,0,13):C.UVGC_250_28,(0,0,4):C.UVGC_250_25,(0,0,5):C.UVGC_250_26,(0,0,10):C.UVGC_250_27,(0,0,13):C.UVGC_250_28,(4,0,4):C.UVGC_254_39,(4,0,5):C.UVGC_254_40,(4,0,10):C.UVGC_254_41,(4,0,13):C.UVGC_254_42,(3,0,4):C.UVGC_254_39,(3,0,5):C.UVGC_254_40,(3,0,10):C.UVGC_254_41,(3,0,13):C.UVGC_254_42,(8,0,4):C.UVGC_250_26,(8,0,5):C.UVGC_250_25,(8,0,10):C.UVGC_251_29,(8,0,13):C.UVGC_251_30,(7,0,0):C.UVGC_458_744,(7,0,2):C.UVGC_458_745,(7,0,3):C.UVGC_458_746,(7,0,4):C.UVGC_459_756,(7,0,5):C.UVGC_459_757,(7,0,6):C.UVGC_458_749,(7,0,7):C.UVGC_458_750,(7,0,8):C.UVGC_458_751,(7,0,9):C.UVGC_459_758,(7,0,11):C.UVGC_459_759,(7,0,12):C.UVGC_459_760,(7,0,14):C.UVGC_459_761,(6,0,0):C.UVGC_458_744,(6,0,2):C.UVGC_458_745,(6,0,3):C.UVGC_458_746,(6,0,4):C.UVGC_458_747,(6,0,5):C.UVGC_458_748,(6,0,6):C.UVGC_458_749,(6,0,7):C.UVGC_458_750,(6,0,8):C.UVGC_458_751,(6,0,9):C.UVGC_458_752,(6,0,11):C.UVGC_458_753,(6,0,12):C.UVGC_458_754,(6,0,14):C.UVGC_458_755,(5,0,4):C.UVGC_254_39,(5,0,5):C.UVGC_254_40,(5,0,10):C.UVGC_254_41,(5,0,13):C.UVGC_254_42,(1,0,4):C.UVGC_254_39,(1,0,5):C.UVGC_254_40,(1,0,10):C.UVGC_254_41,(1,0,13):C.UVGC_254_42,(11,0,4):C.UVGC_249_21,(11,0,5):C.UVGC_249_22,(11,0,10):C.UVGC_249_23,(11,0,13):C.UVGC_249_24,(10,0,4):C.UVGC_249_21,(10,0,5):C.UVGC_249_22,(10,0,10):C.UVGC_249_23,(10,0,13):C.UVGC_249_24,(9,0,4):C.UVGC_242_3,(9,0,5):C.UVGC_242_4,(2,1,4):C.UVGC_250_25,(2,1,5):C.UVGC_250_26,(2,1,10):C.UVGC_250_27,(2,1,13):C.UVGC_250_28,(0,1,4):C.UVGC_250_25,(0,1,5):C.UVGC_250_26,(0,1,10):C.UVGC_250_27,(0,1,13):C.UVGC_250_28,(6,1,0):C.UVGC_455_714,(6,1,2):C.UVGC_455_715,(6,1,3):C.UVGC_455_716,(6,1,4):C.UVGC_455_717,(6,1,5):C.UVGC_455_718,(6,1,6):C.UVGC_455_719,(6,1,7):C.UVGC_455_720,(6,1,8):C.UVGC_455_721,(6,1,9):C.UVGC_455_722,(6,1,11):C.UVGC_455_723,(6,1,12):C.UVGC_455_724,(6,1,14):C.UVGC_455_725,(4,1,4):C.UVGC_254_39,(4,1,5):C.UVGC_254_40,(4,1,10):C.UVGC_254_41,(4,1,13):C.UVGC_254_42,(3,1,4):C.UVGC_254_39,(3,1,5):C.UVGC_254_40,(3,1,10):C.UVGC_254_41,(3,1,13):C.UVGC_254_42,(8,1,0):C.UVGC_457_732,(8,1,2):C.UVGC_457_733,(8,1,3):C.UVGC_457_734,(8,1,4):C.UVGC_457_735,(8,1,5):C.UVGC_457_736,(8,1,6):C.UVGC_457_737,(8,1,7):C.UVGC_457_738,(8,1,8):C.UVGC_457_739,(8,1,9):C.UVGC_457_740,(8,1,11):C.UVGC_457_741,(8,1,12):C.UVGC_457_742,(8,1,14):C.UVGC_457_743,(7,1,1):C.UVGC_252_31,(7,1,4):C.UVGC_253_35,(7,1,5):C.UVGC_253_36,(7,1,10):C.UVGC_253_37,(7,1,13):C.UVGC_253_38,(5,1,4):C.UVGC_254_39,(5,1,5):C.UVGC_254_40,(5,1,10):C.UVGC_254_41,(5,1,13):C.UVGC_254_42,(1,1,4):C.UVGC_254_39,(1,1,5):C.UVGC_254_40,(1,1,10):C.UVGC_254_41,(1,1,13):C.UVGC_254_42,(11,1,4):C.UVGC_249_21,(11,1,5):C.UVGC_249_22,(11,1,10):C.UVGC_249_23,(11,1,13):C.UVGC_249_24,(10,1,4):C.UVGC_249_21,(10,1,5):C.UVGC_249_22,(10,1,10):C.UVGC_249_23,(10,1,13):C.UVGC_249_24,(9,1,4):C.UVGC_242_3,(9,1,5):C.UVGC_242_4,(2,2,4):C.UVGC_250_25,(2,2,5):C.UVGC_250_26,(2,2,10):C.UVGC_250_27,(2,2,13):C.UVGC_250_28,(0,2,4):C.UVGC_250_25,(0,2,5):C.UVGC_250_26,(0,2,10):C.UVGC_250_27,(0,2,13):C.UVGC_250_28,(4,2,4):C.UVGC_254_39,(4,2,5):C.UVGC_254_40,(4,2,10):C.UVGC_254_41,(4,2,13):C.UVGC_254_42,(3,2,4):C.UVGC_254_39,(3,2,5):C.UVGC_254_40,(3,2,10):C.UVGC_254_41,(3,2,13):C.UVGC_254_42,(8,2,0):C.UVGC_454_702,(8,2,2):C.UVGC_454_703,(8,2,3):C.UVGC_454_704,(8,2,4):C.UVGC_454_705,(8,2,5):C.UVGC_454_706,(8,2,6):C.UVGC_454_707,(8,2,7):C.UVGC_454_708,(8,2,8):C.UVGC_454_709,(8,2,9):C.UVGC_454_710,(8,2,11):C.UVGC_454_711,(8,2,12):C.UVGC_454_712,(8,2,14):C.UVGC_454_713,(6,2,1):C.UVGC_252_31,(6,2,4):C.UVGC_252_32,(6,2,5):C.UVGC_242_3,(6,2,10):C.UVGC_252_33,(6,2,13):C.UVGC_252_34,(7,2,0):C.UVGC_455_714,(7,2,2):C.UVGC_455_715,(7,2,3):C.UVGC_455_716,(7,2,4):C.UVGC_456_726,(7,2,5):C.UVGC_456_727,(7,2,6):C.UVGC_455_719,(7,2,7):C.UVGC_455_720,(7,2,8):C.UVGC_455_721,(7,2,9):C.UVGC_456_728,(7,2,11):C.UVGC_456_729,(7,2,12):C.UVGC_456_730,(7,2,14):C.UVGC_456_731,(5,2,4):C.UVGC_254_39,(5,2,5):C.UVGC_254_40,(5,2,10):C.UVGC_254_41,(5,2,13):C.UVGC_254_42,(1,2,4):C.UVGC_254_39,(1,2,5):C.UVGC_254_40,(1,2,10):C.UVGC_254_41,(1,2,13):C.UVGC_254_42,(11,2,4):C.UVGC_249_21,(11,2,5):C.UVGC_249_22,(11,2,10):C.UVGC_249_23,(11,2,13):C.UVGC_249_24,(10,2,4):C.UVGC_249_21,(10,2,5):C.UVGC_249_22,(10,2,10):C.UVGC_249_23,(10,2,13):C.UVGC_249_24,(9,2,4):C.UVGC_242_3,(9,2,5):C.UVGC_242_4})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_423_591,(0,0,2):C.UVGC_423_592,(0,0,1):C.UVGC_423_593,(0,1,0):C.UVGC_424_594,(0,1,2):C.UVGC_424_595,(0,1,1):C.UVGC_424_596})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_394_540,(0,0,2):C.UVGC_394_541,(0,0,0):C.UVGC_394_542,(0,1,1):C.UVGC_393_537,(0,1,2):C.UVGC_393_538,(0,1,0):C.UVGC_393_539})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_440_626,(0,0,2):C.UVGC_440_627,(0,0,1):C.UVGC_440_628,(0,1,0):C.UVGC_441_629,(0,1,2):C.UVGC_441_630,(0,1,1):C.UVGC_441_631})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_410_568,(0,0,2):C.UVGC_410_569,(0,0,1):C.UVGC_410_570,(0,1,0):C.UVGC_409_565,(0,1,2):C.UVGC_409_566,(0,1,1):C.UVGC_409_567})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_443_635,(0,0,2):C.UVGC_443_636,(0,0,1):C.UVGC_443_637,(0,1,0):C.UVGC_444_638,(0,1,2):C.UVGC_444_639,(0,1,1):C.UVGC_444_640})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_372_508})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_390_530})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_406_558})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_371_507})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_389_529})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_405_557})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_388_526,(0,0,2):C.UVGC_388_527,(0,0,0):C.UVGC_388_528,(0,1,1):C.UVGC_391_531,(0,1,2):C.UVGC_391_532,(0,1,0):C.UVGC_391_533})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_404_554,(0,0,2):C.UVGC_404_555,(0,0,1):C.UVGC_404_556,(0,1,0):C.UVGC_407_559,(0,1,2):C.UVGC_407_560,(0,1,1):C.UVGC_407_561})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_421_585,(0,0,2):C.UVGC_421_586,(0,0,1):C.UVGC_421_587,(0,1,0):C.UVGC_418_580,(0,1,2):C.UVGC_418_581,(0,1,1):C.UVGC_418_582})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_437_617,(0,0,2):C.UVGC_437_618,(0,0,1):C.UVGC_437_619,(0,1,0):C.UVGC_433_609,(0,1,2):C.UVGC_433_610,(0,1,1):C.UVGC_433_611})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_438_620,(0,0,2):C.UVGC_438_621,(0,0,1):C.UVGC_438_622,(0,1,0):C.UVGC_434_612,(0,1,2):C.UVGC_434_613,(0,1,1):C.UVGC_434_614})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_379_515})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_419_583})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_435_615})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_380_516})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_420_584})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_436_616})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.a, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_471_825,(0,0,1):C.UVGC_471_826,(0,0,2):C.UVGC_471_827,(0,0,3):C.UVGC_471_828})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.g, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_475_837,(0,0,1):C.UVGC_475_838,(0,0,2):C.UVGC_475_839,(0,0,3):C.UVGC_475_840,(0,0,4):C.UVGC_475_841,(0,0,9):C.UVGC_475_842,(0,0,10):C.UVGC_475_843,(0,0,11):C.UVGC_475_844,(0,0,12):C.UVGC_475_845,(0,0,13):C.UVGC_475_846,(0,0,14):C.UVGC_475_847,(0,0,15):C.UVGC_475_848,(0,0,5):C.UVGC_475_849,(0,0,6):C.UVGC_475_850,(0,0,7):C.UVGC_475_851,(0,0,8):C.UVGC_475_852})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Xd1__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_509_1071,(0,1,2):C.UVGC_509_1072,(0,1,3):C.UVGC_509_1073,(0,1,4):C.UVGC_509_1074,(0,1,1):C.UVGC_509_1075,(0,0,0):C.UVGC_267_62,(0,2,3):C.UVGC_280_75})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_505_1039,(0,1,2):C.UVGC_505_1040,(0,1,3):C.UVGC_505_1041,(0,1,4):C.UVGC_505_1042,(0,1,1):C.UVGC_505_1043,(0,0,0):C.UVGC_265_60,(0,2,4):C.UVGC_296_138})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.a, P.a, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_473_831,(0,0,1):C.UVGC_473_832,(0,0,2):C.UVGC_473_833,(0,0,3):C.UVGC_473_834})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.a, P.g, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_477_855,(0,0,1):C.UVGC_477_856,(0,0,2):C.UVGC_477_857,(0,0,3):C.UVGC_477_858,(0,0,4):C.UVGC_477_859,(0,0,9):C.UVGC_477_860,(0,0,10):C.UVGC_477_861,(0,0,11):C.UVGC_477_862,(0,0,12):C.UVGC_477_863,(0,0,13):C.UVGC_477_864,(0,0,14):C.UVGC_477_865,(0,0,15):C.UVGC_477_866,(0,0,5):C.UVGC_477_867,(0,0,6):C.UVGC_477_868,(0,0,7):C.UVGC_477_869,(0,0,8):C.UVGC_477_870})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_481_891,(0,0,1):C.UVGC_481_892,(0,0,2):C.UVGC_481_893,(0,0,3):C.UVGC_481_894})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_481_891,(0,0,1):C.UVGC_481_892,(0,0,2):C.UVGC_481_893,(0,0,3):C.UVGC_481_894})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_481_891,(0,0,1):C.UVGC_481_892,(0,0,2):C.UVGC_481_893,(0,0,3):C.UVGC_481_894})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.H, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_530_1209,(0,0,1):C.UVGC_530_1210,(0,0,2):C.UVGC_530_1211,(0,0,3):C.UVGC_530_1212})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.g, P.g, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(2,0,0):C.UVGC_479_873,(2,0,1):C.UVGC_479_874,(2,0,2):C.UVGC_479_875,(2,0,3):C.UVGC_479_876,(2,0,4):C.UVGC_479_877,(2,0,9):C.UVGC_479_878,(2,0,10):C.UVGC_479_879,(2,0,11):C.UVGC_479_880,(2,0,12):C.UVGC_479_881,(2,0,13):C.UVGC_479_882,(2,0,14):C.UVGC_479_883,(2,0,15):C.UVGC_479_884,(2,0,5):C.UVGC_479_885,(2,0,6):C.UVGC_479_886,(2,0,7):C.UVGC_479_887,(2,0,8):C.UVGC_479_888,(1,0,0):C.UVGC_479_873,(1,0,1):C.UVGC_479_874,(1,0,2):C.UVGC_479_875,(1,0,3):C.UVGC_479_876,(1,0,4):C.UVGC_479_877,(1,0,9):C.UVGC_479_878,(1,0,10):C.UVGC_479_879,(1,0,11):C.UVGC_479_880,(1,0,12):C.UVGC_479_881,(1,0,13):C.UVGC_479_882,(1,0,14):C.UVGC_479_883,(1,0,15):C.UVGC_479_884,(1,0,5):C.UVGC_479_885,(1,0,6):C.UVGC_479_886,(1,0,7):C.UVGC_479_887,(1,0,8):C.UVGC_479_888,(0,0,3):C.UVGC_264_58,(0,0,5):C.UVGC_264_59})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Xd1, P.Xu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_508_1066,(0,1,2):C.UVGC_508_1067,(0,1,3):C.UVGC_508_1068,(0,1,4):C.UVGC_508_1069,(0,1,1):C.UVGC_508_1070,(0,0,0):C.UVGC_268_63,(0,2,3):C.UVGC_279_74})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Xd1, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_504_1034,(0,1,2):C.UVGC_504_1035,(0,1,3):C.UVGC_504_1036,(0,1,4):C.UVGC_504_1037,(0,1,1):C.UVGC_504_1038,(0,0,0):C.UVGC_266_61,(0,2,4):C.UVGC_295_137})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_494_955,(0,0,3):C.UVGC_494_956,(0,0,4):C.UVGC_494_957,(0,0,5):C.UVGC_494_958,(0,0,1):C.UVGC_494_959,(0,0,2):C.UVGC_494_960})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.a, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_472_829,(0,0,1):C.UVGC_472_830,(0,0,2):C.UVGC_471_827,(0,0,3):C.UVGC_471_828})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_470_820,(0,0,2):C.UVGC_470_821,(0,0,3):C.UVGC_470_822,(0,0,4):C.UVGC_470_823,(0,0,1):C.UVGC_470_824})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_470_820,(0,0,2):C.UVGC_470_821,(0,0,3):C.UVGC_470_822,(0,0,4):C.UVGC_470_823,(0,0,1):C.UVGC_470_824})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_470_820,(0,0,2):C.UVGC_470_821,(0,0,3):C.UVGC_470_822,(0,0,4):C.UVGC_470_823,(0,0,1):C.UVGC_470_824})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.H, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_529_1204,(0,0,2):C.UVGC_529_1205,(0,0,3):C.UVGC_529_1206,(0,0,4):C.UVGC_529_1207,(0,0,1):C.UVGC_529_1208})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.G0, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_484_904,(0,0,2):C.UVGC_484_905,(0,0,3):C.UVGC_484_906,(0,0,4):C.UVGC_484_907,(0,0,1):C.UVGC_484_908})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.g, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_475_837,(0,0,1):C.UVGC_475_838,(0,0,2):C.UVGC_475_839,(0,0,3):C.UVGC_475_840,(0,0,4):C.UVGC_475_841,(0,0,9):C.UVGC_475_842,(0,0,10):C.UVGC_475_843,(0,0,11):C.UVGC_475_844,(0,0,12):C.UVGC_475_845,(0,0,13):C.UVGC_475_846,(0,0,14):C.UVGC_475_847,(0,0,15):C.UVGC_475_848,(0,0,5):C.UVGC_476_853,(0,0,6):C.UVGC_476_854,(0,0,7):C.UVGC_475_851,(0,0,8):C.UVGC_475_852})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Xd2__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_501_1007,(0,1,1):C.UVGC_501_1008,(0,1,3):C.UVGC_501_1009,(0,1,4):C.UVGC_501_1010,(0,1,2):C.UVGC_501_1011,(0,0,1):C.UVGC_273_67,(0,2,3):C.UVGC_278_73})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_497_975,(0,1,1):C.UVGC_497_976,(0,1,3):C.UVGC_497_977,(0,1,4):C.UVGC_497_978,(0,1,2):C.UVGC_497_979,(0,0,1):C.UVGC_271_65,(0,2,4):C.UVGC_294_136})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1], [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu2], [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_495_961,(0,0,6):C.UVGC_495_962,(0,0,7):C.UVGC_495_963,(0,0,8):C.UVGC_495_964,(0,0,1):C.UVGC_495_965,(0,0,4):C.UVGC_495_966,(0,0,5):C.UVGC_495_967,(0,0,2):C.UVGC_495_968,(0,0,3):C.UVGC_495_969})

V_292 = CTVertex(name = 'V_292',
                 type = 'UV',
                 particles = [ P.a, P.a, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_474_835,(0,0,1):C.UVGC_474_836,(0,0,2):C.UVGC_473_833,(0,0,3):C.UVGC_473_834})

V_293 = CTVertex(name = 'V_293',
                 type = 'UV',
                 particles = [ P.a, P.g, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_477_855,(0,0,1):C.UVGC_477_856,(0,0,2):C.UVGC_477_857,(0,0,3):C.UVGC_477_858,(0,0,4):C.UVGC_477_859,(0,0,9):C.UVGC_477_860,(0,0,10):C.UVGC_477_861,(0,0,11):C.UVGC_477_862,(0,0,12):C.UVGC_477_863,(0,0,13):C.UVGC_477_864,(0,0,14):C.UVGC_477_865,(0,0,15):C.UVGC_477_866,(0,0,5):C.UVGC_478_871,(0,0,6):C.UVGC_478_872,(0,0,7):C.UVGC_477_869,(0,0,8):C.UVGC_477_870})

V_294 = CTVertex(name = 'V_294',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_470_820,(0,0,2):C.UVGC_470_821,(0,0,3):C.UVGC_470_822,(0,0,4):C.UVGC_470_823,(0,0,1):C.UVGC_470_824})

V_295 = CTVertex(name = 'V_295',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_470_820,(0,0,2):C.UVGC_470_821,(0,0,3):C.UVGC_470_822,(0,0,4):C.UVGC_470_823,(0,0,1):C.UVGC_470_824})

V_296 = CTVertex(name = 'V_296',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_470_820,(0,0,2):C.UVGC_470_821,(0,0,3):C.UVGC_470_822,(0,0,4):C.UVGC_470_823,(0,0,1):C.UVGC_470_824})

V_297 = CTVertex(name = 'V_297',
                 type = 'UV',
                 particles = [ P.H, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_529_1204,(0,0,2):C.UVGC_529_1205,(0,0,3):C.UVGC_529_1206,(0,0,4):C.UVGC_529_1207,(0,0,1):C.UVGC_529_1208})

V_298 = CTVertex(name = 'V_298',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_482_895,(0,0,1):C.UVGC_482_896,(0,0,2):C.UVGC_482_897,(0,0,3):C.UVGC_482_898})

V_299 = CTVertex(name = 'V_299',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_482_895,(0,0,1):C.UVGC_482_896,(0,0,2):C.UVGC_482_897,(0,0,3):C.UVGC_482_898})

V_300 = CTVertex(name = 'V_300',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_482_895,(0,0,1):C.UVGC_482_896,(0,0,2):C.UVGC_482_897,(0,0,3):C.UVGC_482_898})

V_301 = CTVertex(name = 'V_301',
                 type = 'UV',
                 particles = [ P.H, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_531_1213,(0,0,1):C.UVGC_531_1214,(0,0,2):C.UVGC_531_1215,(0,0,3):C.UVGC_531_1216})

V_302 = CTVertex(name = 'V_302',
                 type = 'UV',
                 particles = [ P.G0, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_483_899,(0,0,2):C.UVGC_483_900,(0,0,3):C.UVGC_483_901,(0,0,4):C.UVGC_483_902,(0,0,1):C.UVGC_483_903})

V_303 = CTVertex(name = 'V_303',
                 type = 'UV',
                 particles = [ P.g, P.g, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(2,0,0):C.UVGC_479_873,(2,0,1):C.UVGC_479_874,(2,0,2):C.UVGC_479_875,(2,0,3):C.UVGC_479_876,(2,0,4):C.UVGC_479_877,(2,0,9):C.UVGC_479_878,(2,0,10):C.UVGC_479_879,(2,0,11):C.UVGC_479_880,(2,0,12):C.UVGC_479_881,(2,0,13):C.UVGC_479_882,(2,0,14):C.UVGC_479_883,(2,0,15):C.UVGC_479_884,(2,0,5):C.UVGC_480_889,(2,0,6):C.UVGC_480_890,(2,0,7):C.UVGC_479_887,(2,0,8):C.UVGC_479_888,(1,0,0):C.UVGC_479_873,(1,0,1):C.UVGC_479_874,(1,0,2):C.UVGC_479_875,(1,0,3):C.UVGC_479_876,(1,0,4):C.UVGC_479_877,(1,0,9):C.UVGC_479_878,(1,0,10):C.UVGC_479_879,(1,0,11):C.UVGC_479_880,(1,0,12):C.UVGC_479_881,(1,0,13):C.UVGC_479_882,(1,0,14):C.UVGC_479_883,(1,0,15):C.UVGC_479_884,(1,0,5):C.UVGC_480_889,(1,0,6):C.UVGC_480_890,(1,0,7):C.UVGC_479_887,(1,0,8):C.UVGC_479_888,(0,0,3):C.UVGC_264_58,(0,0,6):C.UVGC_264_59})

V_304 = CTVertex(name = 'V_304',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Xd2, P.Xu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_500_1002,(0,1,1):C.UVGC_500_1003,(0,1,3):C.UVGC_500_1004,(0,1,4):C.UVGC_500_1005,(0,1,2):C.UVGC_500_1006,(0,0,1):C.UVGC_274_68,(0,2,3):C.UVGC_277_72})

V_305 = CTVertex(name = 'V_305',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Xd2, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,1,0):C.UVGC_496_970,(0,1,1):C.UVGC_496_971,(0,1,3):C.UVGC_496_972,(0,1,4):C.UVGC_496_973,(0,1,2):C.UVGC_496_974,(0,0,1):C.UVGC_272_66,(0,2,4):C.UVGC_293_135})

V_306 = CTVertex(name = 'V_306',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1], [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu2], [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_495_961,(0,0,6):C.UVGC_495_962,(0,0,7):C.UVGC_495_963,(0,0,8):C.UVGC_495_964,(0,0,1):C.UVGC_495_965,(0,0,4):C.UVGC_495_966,(0,0,5):C.UVGC_495_967,(0,0,2):C.UVGC_495_968,(0,0,3):C.UVGC_495_969})

V_307 = CTVertex(name = 'V_307',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_493_949,(0,0,1):C.UVGC_493_950,(0,0,4):C.UVGC_493_951,(0,0,5):C.UVGC_493_952,(0,0,2):C.UVGC_493_953,(0,0,3):C.UVGC_493_954})

V_308 = CTVertex(name = 'V_308',
                 type = 'UV',
                 particles = [ P.a, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_282_77})

V_309 = CTVertex(name = 'V_309',
                 type = 'UV',
                 particles = [ P.G__plus__, P.Xd1, P.Xu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_486_914,(0,0,2):C.UVGC_486_915,(0,0,3):C.UVGC_486_916,(0,0,4):C.UVGC_486_917,(0,0,1):C.UVGC_486_918})

V_310 = CTVertex(name = 'V_310',
                 type = 'UV',
                 particles = [ P.G__plus__, P.Xd2, P.Xu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_489_929,(0,0,1):C.UVGC_489_930,(0,0,3):C.UVGC_489_931,(0,0,4):C.UVGC_489_932,(0,0,2):C.UVGC_489_933})

V_311 = CTVertex(name = 'V_311',
                 type = 'UV',
                 particles = [ P.g, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_284_79,(0,0,1):C.UVGC_284_80,(0,0,2):C.UVGC_284_81,(0,0,3):C.UVGC_284_82,(0,0,4):C.UVGC_284_83,(0,0,6):C.UVGC_284_84,(0,0,7):C.UVGC_284_85,(0,0,8):C.UVGC_284_86,(0,0,9):C.UVGC_284_87,(0,0,10):C.UVGC_284_88,(0,0,11):C.UVGC_284_89,(0,0,12):C.UVGC_284_90,(0,0,5):C.UVGC_284_91})

V_312 = CTVertex(name = 'V_312',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.Xd1, P.Xu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_511_1081,(0,0,1):C.UVGC_511_1082,(0,0,2):C.UVGC_511_1083,(0,0,3):C.UVGC_511_1084,(0,0,4):C.UVGC_511_1085,(0,0,10):C.UVGC_511_1086,(0,0,11):C.UVGC_511_1087,(0,0,12):C.UVGC_511_1088,(0,0,13):C.UVGC_511_1089,(0,0,14):C.UVGC_511_1090,(0,0,15):C.UVGC_511_1091,(0,0,16):C.UVGC_511_1092,(0,0,5):C.UVGC_511_1093,(0,0,7):C.UVGC_511_1094,(0,0,8):C.UVGC_511_1095,(0,0,9):C.UVGC_511_1096,(0,0,6):C.UVGC_511_1097})

V_313 = CTVertex(name = 'V_313',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.Xd2, P.Xu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_503_1017,(0,0,1):C.UVGC_503_1018,(0,0,2):C.UVGC_503_1019,(0,0,3):C.UVGC_503_1020,(0,0,4):C.UVGC_503_1021,(0,0,10):C.UVGC_503_1022,(0,0,11):C.UVGC_503_1023,(0,0,12):C.UVGC_503_1024,(0,0,13):C.UVGC_503_1025,(0,0,14):C.UVGC_503_1026,(0,0,15):C.UVGC_503_1027,(0,0,16):C.UVGC_503_1028,(0,0,5):C.UVGC_503_1029,(0,0,6):C.UVGC_503_1030,(0,0,8):C.UVGC_503_1031,(0,0,9):C.UVGC_503_1032,(0,0,7):C.UVGC_503_1033})

V_314 = CTVertex(name = 'V_314',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.Xd1, P.Xu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_510_1076,(0,0,2):C.UVGC_510_1077,(0,0,3):C.UVGC_510_1078,(0,0,4):C.UVGC_510_1079,(0,0,1):C.UVGC_510_1080})

V_315 = CTVertex(name = 'V_315',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.Xd2, P.Xu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_502_1012,(0,0,1):C.UVGC_502_1013,(0,0,3):C.UVGC_502_1014,(0,0,4):C.UVGC_502_1015,(0,0,2):C.UVGC_502_1016})

V_316 = CTVertex(name = 'V_316',
                 type = 'UV',
                 particles = [ P.a, P.a, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_283_78})

V_317 = CTVertex(name = 'V_317',
                 type = 'UV',
                 particles = [ P.a, P.g, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_285_92,(0,0,1):C.UVGC_285_93,(0,0,2):C.UVGC_285_94,(0,0,3):C.UVGC_285_95,(0,0,4):C.UVGC_285_96,(0,0,6):C.UVGC_285_97,(0,0,7):C.UVGC_285_98,(0,0,8):C.UVGC_285_99,(0,0,9):C.UVGC_285_100,(0,0,10):C.UVGC_285_101,(0,0,11):C.UVGC_285_102,(0,0,12):C.UVGC_285_103,(0,0,5):C.UVGC_285_104})

V_318 = CTVertex(name = 'V_318',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_287_118})

V_319 = CTVertex(name = 'V_319',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_287_118})

V_320 = CTVertex(name = 'V_320',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_287_118})

V_321 = CTVertex(name = 'V_321',
                 type = 'UV',
                 particles = [ P.H, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_462_765,(0,0,1):C.UVGC_462_766})

V_322 = CTVertex(name = 'V_322',
                 type = 'UV',
                 particles = [ P.G__minus__, P.Xd1__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_485_909,(0,0,2):C.UVGC_485_910,(0,0,3):C.UVGC_485_911,(0,0,4):C.UVGC_485_912,(0,0,1):C.UVGC_485_913})

V_323 = CTVertex(name = 'V_323',
                 type = 'UV',
                 particles = [ P.G__minus__, P.Xd2__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_490_934,(0,0,1):C.UVGC_490_935,(0,0,3):C.UVGC_490_936,(0,0,4):C.UVGC_490_937,(0,0,2):C.UVGC_490_938})

V_324 = CTVertex(name = 'V_324',
                 type = 'UV',
                 particles = [ P.g, P.g, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(2,0,0):C.UVGC_286_105,(2,0,1):C.UVGC_286_106,(2,0,2):C.UVGC_286_107,(2,0,3):C.UVGC_286_108,(2,0,4):C.UVGC_286_109,(2,0,6):C.UVGC_286_110,(2,0,7):C.UVGC_286_111,(2,0,8):C.UVGC_286_112,(2,0,9):C.UVGC_286_113,(2,0,10):C.UVGC_286_114,(2,0,11):C.UVGC_286_115,(2,0,12):C.UVGC_286_116,(2,0,5):C.UVGC_286_117,(1,0,0):C.UVGC_286_105,(1,0,1):C.UVGC_286_106,(1,0,2):C.UVGC_286_107,(1,0,3):C.UVGC_286_108,(1,0,4):C.UVGC_286_109,(1,0,6):C.UVGC_286_110,(1,0,7):C.UVGC_286_111,(1,0,8):C.UVGC_286_112,(1,0,9):C.UVGC_286_113,(1,0,10):C.UVGC_286_114,(1,0,11):C.UVGC_286_115,(1,0,12):C.UVGC_286_116,(1,0,5):C.UVGC_286_117,(0,0,3):C.UVGC_276_70,(0,0,5):C.UVGC_276_71})

V_325 = CTVertex(name = 'V_325',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.Xd1__tilde__, P.Xu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_511_1081,(0,0,1):C.UVGC_511_1082,(0,0,2):C.UVGC_511_1083,(0,0,3):C.UVGC_511_1084,(0,0,4):C.UVGC_511_1085,(0,0,10):C.UVGC_511_1086,(0,0,11):C.UVGC_511_1087,(0,0,12):C.UVGC_511_1088,(0,0,13):C.UVGC_511_1089,(0,0,14):C.UVGC_511_1090,(0,0,15):C.UVGC_511_1091,(0,0,16):C.UVGC_511_1092,(0,0,5):C.UVGC_511_1093,(0,0,7):C.UVGC_511_1094,(0,0,8):C.UVGC_511_1095,(0,0,9):C.UVGC_511_1096,(0,0,6):C.UVGC_511_1097})

V_326 = CTVertex(name = 'V_326',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.Xd2__tilde__, P.Xu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_503_1017,(0,0,1):C.UVGC_503_1018,(0,0,2):C.UVGC_503_1019,(0,0,3):C.UVGC_503_1020,(0,0,4):C.UVGC_503_1021,(0,0,10):C.UVGC_503_1022,(0,0,11):C.UVGC_503_1023,(0,0,12):C.UVGC_503_1024,(0,0,13):C.UVGC_503_1025,(0,0,14):C.UVGC_503_1026,(0,0,15):C.UVGC_503_1027,(0,0,16):C.UVGC_503_1028,(0,0,5):C.UVGC_503_1029,(0,0,6):C.UVGC_503_1030,(0,0,8):C.UVGC_503_1031,(0,0,9):C.UVGC_503_1032,(0,0,7):C.UVGC_503_1033})

V_327 = CTVertex(name = 'V_327',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.Xd1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_510_1076,(0,0,2):C.UVGC_510_1077,(0,0,3):C.UVGC_510_1078,(0,0,4):C.UVGC_510_1079,(0,0,1):C.UVGC_510_1080})

V_328 = CTVertex(name = 'V_328',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.Xd2__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_502_1012,(0,0,1):C.UVGC_502_1013,(0,0,3):C.UVGC_502_1014,(0,0,4):C.UVGC_502_1015,(0,0,2):C.UVGC_502_1016})

V_329 = CTVertex(name = 'V_329',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_319_191,(0,0,2):C.UVGC_319_192,(0,0,4):C.UVGC_319_193,(0,0,1):C.UVGC_319_194,(0,0,3):C.UVGC_319_195})

V_330 = CTVertex(name = 'V_330',
                 type = 'UV',
                 particles = [ P.a, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_298_140})

V_331 = CTVertex(name = 'V_331',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_320_196,(0,0,2):C.UVGC_320_197,(0,0,1):C.UVGC_320_198})

V_332 = CTVertex(name = 'V_332',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_320_196,(0,0,2):C.UVGC_320_197,(0,0,1):C.UVGC_320_198})

V_333 = CTVertex(name = 'V_333',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_320_196,(0,0,2):C.UVGC_320_197,(0,0,1):C.UVGC_320_198})

V_334 = CTVertex(name = 'V_334',
                 type = 'UV',
                 particles = [ P.H, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_464_770,(0,0,2):C.UVGC_464_771,(0,0,1):C.UVGC_464_772})

V_335 = CTVertex(name = 'V_335',
                 type = 'UV',
                 particles = [ P.G0, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_463_767,(0,0,2):C.UVGC_463_768,(0,0,1):C.UVGC_463_769})

V_336 = CTVertex(name = 'V_336',
                 type = 'UV',
                 particles = [ P.G__plus__, P.Xd1, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_492_944,(0,0,2):C.UVGC_492_945,(0,0,3):C.UVGC_492_946,(0,0,4):C.UVGC_492_947,(0,0,1):C.UVGC_492_948})

V_337 = CTVertex(name = 'V_337',
                 type = 'UV',
                 particles = [ P.G__plus__, P.Xd2, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_488_924,(0,0,1):C.UVGC_488_925,(0,0,3):C.UVGC_488_926,(0,0,4):C.UVGC_488_927,(0,0,2):C.UVGC_488_928})

V_338 = CTVertex(name = 'V_338',
                 type = 'UV',
                 particles = [ P.g, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_284_79,(0,0,1):C.UVGC_284_80,(0,0,2):C.UVGC_284_81,(0,0,3):C.UVGC_284_82,(0,0,4):C.UVGC_284_83,(0,0,6):C.UVGC_284_84,(0,0,7):C.UVGC_284_85,(0,0,8):C.UVGC_284_86,(0,0,9):C.UVGC_284_87,(0,0,10):C.UVGC_284_88,(0,0,11):C.UVGC_284_89,(0,0,12):C.UVGC_284_90,(0,0,5):C.UVGC_300_142})

V_339 = CTVertex(name = 'V_339',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.Xd1, P.Xu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_507_1049,(0,0,1):C.UVGC_507_1050,(0,0,2):C.UVGC_507_1051,(0,0,3):C.UVGC_507_1052,(0,0,4):C.UVGC_507_1053,(0,0,10):C.UVGC_507_1054,(0,0,11):C.UVGC_507_1055,(0,0,12):C.UVGC_507_1056,(0,0,13):C.UVGC_507_1057,(0,0,14):C.UVGC_507_1058,(0,0,15):C.UVGC_507_1059,(0,0,16):C.UVGC_507_1060,(0,0,5):C.UVGC_507_1061,(0,0,7):C.UVGC_507_1062,(0,0,8):C.UVGC_507_1063,(0,0,9):C.UVGC_507_1064,(0,0,6):C.UVGC_507_1065})

V_340 = CTVertex(name = 'V_340',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.Xd2, P.Xu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_499_985,(0,0,1):C.UVGC_499_986,(0,0,2):C.UVGC_499_987,(0,0,3):C.UVGC_499_988,(0,0,4):C.UVGC_499_989,(0,0,10):C.UVGC_499_990,(0,0,11):C.UVGC_499_991,(0,0,12):C.UVGC_499_992,(0,0,13):C.UVGC_499_993,(0,0,14):C.UVGC_499_994,(0,0,15):C.UVGC_499_995,(0,0,16):C.UVGC_499_996,(0,0,5):C.UVGC_499_997,(0,0,6):C.UVGC_499_998,(0,0,8):C.UVGC_499_999,(0,0,9):C.UVGC_499_1000,(0,0,7):C.UVGC_499_1001})

V_341 = CTVertex(name = 'V_341',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.Xd1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_506_1044,(0,0,2):C.UVGC_506_1045,(0,0,3):C.UVGC_506_1046,(0,0,4):C.UVGC_506_1047,(0,0,1):C.UVGC_506_1048})

V_342 = CTVertex(name = 'V_342',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.Xd2, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_498_980,(0,0,1):C.UVGC_498_981,(0,0,3):C.UVGC_498_982,(0,0,4):C.UVGC_498_983,(0,0,2):C.UVGC_498_984})

V_343 = CTVertex(name = 'V_343',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1], [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1], [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_250,(0,0,3):C.UVGC_334_251,(0,0,6):C.UVGC_334_252,(0,0,8):C.UVGC_334_253,(0,0,1):C.UVGC_334_254,(0,0,4):C.UVGC_334_255,(0,0,7):C.UVGC_334_256,(0,0,2):C.UVGC_334_257,(0,0,5):C.UVGC_334_258})

V_344 = CTVertex(name = 'V_344',
                 type = 'UV',
                 particles = [ P.a, P.a, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_299_141})

V_345 = CTVertex(name = 'V_345',
                 type = 'UV',
                 particles = [ P.a, P.g, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_285_92,(0,0,1):C.UVGC_285_93,(0,0,2):C.UVGC_285_94,(0,0,3):C.UVGC_285_95,(0,0,4):C.UVGC_285_96,(0,0,6):C.UVGC_285_97,(0,0,7):C.UVGC_285_98,(0,0,8):C.UVGC_285_99,(0,0,9):C.UVGC_285_100,(0,0,10):C.UVGC_285_101,(0,0,11):C.UVGC_285_102,(0,0,12):C.UVGC_285_103,(0,0,5):C.UVGC_301_143})

V_346 = CTVertex(name = 'V_346',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_320_196,(0,0,2):C.UVGC_320_197,(0,0,1):C.UVGC_320_198})

V_347 = CTVertex(name = 'V_347',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_320_196,(0,0,2):C.UVGC_320_197,(0,0,1):C.UVGC_320_198})

V_348 = CTVertex(name = 'V_348',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_320_196,(0,0,2):C.UVGC_320_197,(0,0,1):C.UVGC_320_198})

V_349 = CTVertex(name = 'V_349',
                 type = 'UV',
                 particles = [ P.H, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_464_770,(0,0,2):C.UVGC_464_771,(0,0,1):C.UVGC_464_772})

V_350 = CTVertex(name = 'V_350',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_303_145})

V_351 = CTVertex(name = 'V_351',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_303_145})

V_352 = CTVertex(name = 'V_352',
                 type = 'UV',
                 particles = [ P.H, P.H, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_303_145})

V_353 = CTVertex(name = 'V_353',
                 type = 'UV',
                 particles = [ P.H, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_461_763,(0,0,1):C.UVGC_461_764})

V_354 = CTVertex(name = 'V_354',
                 type = 'UV',
                 particles = [ P.G__minus__, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_491_939,(0,0,2):C.UVGC_491_940,(0,0,3):C.UVGC_491_941,(0,0,4):C.UVGC_491_942,(0,0,1):C.UVGC_491_943})

V_355 = CTVertex(name = 'V_355',
                 type = 'UV',
                 particles = [ P.G__minus__, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_487_919,(0,0,1):C.UVGC_487_920,(0,0,3):C.UVGC_487_921,(0,0,4):C.UVGC_487_922,(0,0,2):C.UVGC_487_923})

V_356 = CTVertex(name = 'V_356',
                 type = 'UV',
                 particles = [ P.G0, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_465_773,(0,0,2):C.UVGC_465_774,(0,0,1):C.UVGC_465_775})

V_357 = CTVertex(name = 'V_357',
                 type = 'UV',
                 particles = [ P.g, P.g, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(2,0,0):C.UVGC_286_105,(2,0,1):C.UVGC_286_106,(2,0,2):C.UVGC_286_107,(2,0,3):C.UVGC_286_108,(2,0,4):C.UVGC_286_109,(2,0,6):C.UVGC_286_110,(2,0,7):C.UVGC_286_111,(2,0,8):C.UVGC_286_112,(2,0,9):C.UVGC_286_113,(2,0,10):C.UVGC_286_114,(2,0,11):C.UVGC_286_115,(2,0,12):C.UVGC_286_116,(2,0,5):C.UVGC_302_144,(1,0,0):C.UVGC_286_105,(1,0,1):C.UVGC_286_106,(1,0,2):C.UVGC_286_107,(1,0,3):C.UVGC_286_108,(1,0,4):C.UVGC_286_109,(1,0,6):C.UVGC_286_110,(1,0,7):C.UVGC_286_111,(1,0,8):C.UVGC_286_112,(1,0,9):C.UVGC_286_113,(1,0,10):C.UVGC_286_114,(1,0,11):C.UVGC_286_115,(1,0,12):C.UVGC_286_116,(1,0,5):C.UVGC_302_144,(0,0,3):C.UVGC_276_70,(0,0,5):C.UVGC_276_71})

V_358 = CTVertex(name = 'V_358',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_507_1049,(0,0,1):C.UVGC_507_1050,(0,0,2):C.UVGC_507_1051,(0,0,3):C.UVGC_507_1052,(0,0,4):C.UVGC_507_1053,(0,0,10):C.UVGC_507_1054,(0,0,11):C.UVGC_507_1055,(0,0,12):C.UVGC_507_1056,(0,0,13):C.UVGC_507_1057,(0,0,14):C.UVGC_507_1058,(0,0,15):C.UVGC_507_1059,(0,0,16):C.UVGC_507_1060,(0,0,5):C.UVGC_507_1061,(0,0,7):C.UVGC_507_1062,(0,0,8):C.UVGC_507_1063,(0,0,9):C.UVGC_507_1064,(0,0,6):C.UVGC_507_1065})

V_359 = CTVertex(name = 'V_359',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_499_985,(0,0,1):C.UVGC_499_986,(0,0,2):C.UVGC_499_987,(0,0,3):C.UVGC_499_988,(0,0,4):C.UVGC_499_989,(0,0,10):C.UVGC_499_990,(0,0,11):C.UVGC_499_991,(0,0,12):C.UVGC_499_992,(0,0,13):C.UVGC_499_993,(0,0,14):C.UVGC_499_994,(0,0,15):C.UVGC_499_995,(0,0,16):C.UVGC_499_996,(0,0,5):C.UVGC_499_997,(0,0,6):C.UVGC_499_998,(0,0,8):C.UVGC_499_999,(0,0,9):C.UVGC_499_1000,(0,0,7):C.UVGC_499_1001})

V_360 = CTVertex(name = 'V_360',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_506_1044,(0,0,2):C.UVGC_506_1045,(0,0,3):C.UVGC_506_1046,(0,0,4):C.UVGC_506_1047,(0,0,1):C.UVGC_506_1048})

V_361 = CTVertex(name = 'V_361',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_498_980,(0,0,1):C.UVGC_498_981,(0,0,3):C.UVGC_498_982,(0,0,4):C.UVGC_498_983,(0,0,2):C.UVGC_498_984})

V_362 = CTVertex(name = 'V_362',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1], [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1], [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_250,(0,0,3):C.UVGC_334_251,(0,0,6):C.UVGC_334_252,(0,0,8):C.UVGC_334_253,(0,0,1):C.UVGC_334_254,(0,0,4):C.UVGC_334_255,(0,0,7):C.UVGC_334_256,(0,0,2):C.UVGC_334_257,(0,0,5):C.UVGC_334_258})

V_363 = CTVertex(name = 'V_363',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_318_186,(0,0,2):C.UVGC_318_187,(0,0,4):C.UVGC_318_188,(0,0,1):C.UVGC_318_189,(0,0,3):C.UVGC_318_190})

V_364 = CTVertex(name = 'V_364',
                 type = 'UV',
                 particles = [ P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_518_1134,(0,0,1):C.UVGC_518_1135,(0,0,2):C.UVGC_518_1136,(0,0,3):C.UVGC_518_1137,(0,1,0):C.UVGC_519_1138,(0,1,1):C.UVGC_519_1139,(0,1,2):C.UVGC_519_1140,(0,1,3):C.UVGC_519_1141})

V_365 = CTVertex(name = 'V_365',
                 type = 'UV',
                 particles = [ P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_512_1098,(0,0,2):C.UVGC_512_1099,(0,0,3):C.UVGC_512_1100,(0,0,4):C.UVGC_512_1101,(0,0,1):C.UVGC_512_1102,(0,1,0):C.UVGC_515_1110,(0,1,2):C.UVGC_515_1111,(0,1,3):C.UVGC_514_1107,(0,1,4):C.UVGC_514_1108,(0,1,1):C.UVGC_514_1109})

V_366 = CTVertex(name = 'V_366',
                 type = 'UV',
                 particles = [ P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_514_1105,(0,0,2):C.UVGC_514_1106,(0,0,3):C.UVGC_514_1107,(0,0,4):C.UVGC_514_1108,(0,0,1):C.UVGC_514_1109,(0,1,0):C.UVGC_513_1103,(0,1,2):C.UVGC_513_1104,(0,1,3):C.UVGC_512_1100,(0,1,4):C.UVGC_512_1101,(0,1,1):C.UVGC_512_1102})

V_367 = CTVertex(name = 'V_367',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_522_1150,(0,0,1):C.UVGC_522_1151,(0,0,2):C.UVGC_522_1152,(0,0,3):C.UVGC_522_1153})

V_368 = CTVertex(name = 'V_368',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_524_1158,(0,0,1):C.UVGC_524_1159,(0,0,2):C.UVGC_524_1160,(0,0,3):C.UVGC_524_1161,(0,0,4):C.UVGC_524_1162,(0,0,9):C.UVGC_524_1163,(0,0,10):C.UVGC_524_1164,(0,0,11):C.UVGC_524_1165,(0,0,12):C.UVGC_524_1166,(0,0,13):C.UVGC_524_1167,(0,0,14):C.UVGC_524_1168,(0,0,15):C.UVGC_524_1169,(0,0,5):C.UVGC_524_1170,(0,0,6):C.UVGC_524_1171,(0,0,7):C.UVGC_524_1172,(0,0,8):C.UVGC_524_1173})

V_369 = CTVertex(name = 'V_369',
                 type = 'UV',
                 particles = [ P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_521_1146,(0,0,1):C.UVGC_521_1147,(0,0,2):C.UVGC_521_1148,(0,0,3):C.UVGC_521_1149,(0,1,0):C.UVGC_520_1142,(0,1,1):C.UVGC_520_1143,(0,1,2):C.UVGC_520_1144,(0,1,3):C.UVGC_520_1145})

V_370 = CTVertex(name = 'V_370',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_516_1112,(0,0,2):C.UVGC_516_1113,(0,0,3):C.UVGC_516_1114,(0,0,4):C.UVGC_516_1115,(0,0,1):C.UVGC_516_1116})

V_371 = CTVertex(name = 'V_371',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_517_1117,(0,0,1):C.UVGC_517_1118,(0,0,2):C.UVGC_517_1119,(0,0,3):C.UVGC_517_1120,(0,0,4):C.UVGC_517_1121,(0,0,10):C.UVGC_517_1122,(0,0,11):C.UVGC_517_1123,(0,0,12):C.UVGC_517_1124,(0,0,13):C.UVGC_517_1125,(0,0,14):C.UVGC_517_1126,(0,0,15):C.UVGC_517_1127,(0,0,16):C.UVGC_517_1128,(0,0,5):C.UVGC_517_1129,(0,0,7):C.UVGC_517_1130,(0,0,8):C.UVGC_517_1131,(0,0,9):C.UVGC_517_1132,(0,0,6):C.UVGC_517_1133})

V_372 = CTVertex(name = 'V_372',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_516_1112,(0,0,2):C.UVGC_516_1113,(0,0,3):C.UVGC_516_1114,(0,0,4):C.UVGC_516_1115,(0,0,1):C.UVGC_516_1116})

V_373 = CTVertex(name = 'V_373',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_517_1117,(0,0,1):C.UVGC_517_1118,(0,0,2):C.UVGC_517_1119,(0,0,3):C.UVGC_517_1120,(0,0,4):C.UVGC_517_1121,(0,0,10):C.UVGC_517_1122,(0,0,11):C.UVGC_517_1123,(0,0,12):C.UVGC_517_1124,(0,0,13):C.UVGC_517_1125,(0,0,14):C.UVGC_517_1126,(0,0,15):C.UVGC_517_1127,(0,0,16):C.UVGC_517_1128,(0,0,5):C.UVGC_517_1129,(0,0,7):C.UVGC_517_1130,(0,0,8):C.UVGC_517_1131,(0,0,9):C.UVGC_517_1132,(0,0,6):C.UVGC_517_1133})

V_374 = CTVertex(name = 'V_374',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_523_1154,(0,0,1):C.UVGC_523_1155,(0,0,2):C.UVGC_523_1156,(0,0,3):C.UVGC_523_1157})

V_375 = CTVertex(name = 'V_375',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_525_1174,(0,0,1):C.UVGC_525_1175,(0,0,2):C.UVGC_525_1176,(0,0,3):C.UVGC_525_1177,(0,0,4):C.UVGC_525_1178,(0,0,9):C.UVGC_525_1179,(0,0,10):C.UVGC_525_1180,(0,0,11):C.UVGC_525_1181,(0,0,12):C.UVGC_525_1182,(0,0,13):C.UVGC_525_1183,(0,0,14):C.UVGC_525_1184,(0,0,15):C.UVGC_525_1185,(0,0,5):C.UVGC_525_1186,(0,0,6):C.UVGC_525_1187,(0,0,7):C.UVGC_525_1188,(0,0,8):C.UVGC_525_1189})

V_376 = CTVertex(name = 'V_376',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_527_1195,(0,0,2):C.UVGC_527_1196,(0,0,3):C.UVGC_527_1197,(0,0,4):C.UVGC_527_1198,(0,0,1):C.UVGC_527_1199})

V_377 = CTVertex(name = 'V_377',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_526_1190,(0,0,2):C.UVGC_526_1191,(0,0,3):C.UVGC_526_1192,(0,0,4):C.UVGC_526_1193,(0,0,1):C.UVGC_526_1194})

V_378 = CTVertex(name = 'V_378',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xd1__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_526_1190,(0,0,2):C.UVGC_526_1191,(0,0,3):C.UVGC_526_1192,(0,0,4):C.UVGC_526_1193,(0,0,1):C.UVGC_526_1194})

V_379 = CTVertex(name = 'V_379',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_528_1200,(0,0,2):C.UVGC_528_1201,(0,0,3):C.UVGC_528_1202,(0,0,4):C.UVGC_528_1203,(0,0,1):C.UVGC_527_1199})

V_380 = CTVertex(name = 'V_380',
                 type = 'UV',
                 particles = [ P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_288_119,(0,1,0):C.UVGC_289_120})

V_381 = CTVertex(name = 'V_381',
                 type = 'UV',
                 particles = [ P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_323_204,(0,0,2):C.UVGC_323_205,(0,0,1):C.UVGC_323_206,(0,1,0):C.UVGC_322_202,(0,1,2):C.UVGC_322_203,(0,1,1):C.UVGC_321_201})

V_382 = CTVertex(name = 'V_382',
                 type = 'UV',
                 particles = [ P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_321_199,(0,0,2):C.UVGC_321_200,(0,0,1):C.UVGC_321_201,(0,1,0):C.UVGC_324_207,(0,1,2):C.UVGC_324_208,(0,1,1):C.UVGC_323_206})

V_383 = CTVertex(name = 'V_383',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_290_121})

V_384 = CTVertex(name = 'V_384',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_291_122,(0,0,1):C.UVGC_291_123,(0,0,2):C.UVGC_291_124,(0,0,3):C.UVGC_291_125,(0,0,4):C.UVGC_291_126,(0,0,6):C.UVGC_291_127,(0,0,7):C.UVGC_291_128,(0,0,8):C.UVGC_291_129,(0,0,9):C.UVGC_291_130,(0,0,10):C.UVGC_291_131,(0,0,11):C.UVGC_291_132,(0,0,12):C.UVGC_291_133,(0,0,5):C.UVGC_291_134})

V_385 = CTVertex(name = 'V_385',
                 type = 'UV',
                 particles = [ P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_304_146,(0,1,0):C.UVGC_305_147})

V_386 = CTVertex(name = 'V_386',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_325_209,(0,0,2):C.UVGC_325_210,(0,0,1):C.UVGC_325_211})

V_387 = CTVertex(name = 'V_387',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_326_212,(0,0,1):C.UVGC_326_213,(0,0,2):C.UVGC_326_214,(0,0,3):C.UVGC_326_215,(0,0,4):C.UVGC_326_216,(0,0,8):C.UVGC_326_217,(0,0,9):C.UVGC_326_218,(0,0,10):C.UVGC_326_219,(0,0,11):C.UVGC_326_220,(0,0,12):C.UVGC_326_221,(0,0,13):C.UVGC_326_222,(0,0,14):C.UVGC_326_223,(0,0,5):C.UVGC_326_224,(0,0,7):C.UVGC_326_225,(0,0,6):C.UVGC_326_226})

V_388 = CTVertex(name = 'V_388',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_325_209,(0,0,2):C.UVGC_325_210,(0,0,1):C.UVGC_325_211})

V_389 = CTVertex(name = 'V_389',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_326_212,(0,0,1):C.UVGC_326_213,(0,0,2):C.UVGC_326_214,(0,0,3):C.UVGC_326_215,(0,0,4):C.UVGC_326_216,(0,0,8):C.UVGC_326_217,(0,0,9):C.UVGC_326_218,(0,0,10):C.UVGC_326_219,(0,0,11):C.UVGC_326_220,(0,0,12):C.UVGC_326_221,(0,0,13):C.UVGC_326_222,(0,0,14):C.UVGC_326_223,(0,0,5):C.UVGC_326_224,(0,0,7):C.UVGC_326_225,(0,0,6):C.UVGC_326_226})

V_390 = CTVertex(name = 'V_390',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_306_148})

V_391 = CTVertex(name = 'V_391',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.Xu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_307_149,(0,0,1):C.UVGC_307_150,(0,0,2):C.UVGC_307_151,(0,0,3):C.UVGC_307_152,(0,0,4):C.UVGC_307_153,(0,0,6):C.UVGC_307_154,(0,0,7):C.UVGC_307_155,(0,0,8):C.UVGC_307_156,(0,0,9):C.UVGC_307_157,(0,0,10):C.UVGC_307_158,(0,0,11):C.UVGC_307_159,(0,0,12):C.UVGC_307_160,(0,0,5):C.UVGC_307_161})

V_392 = CTVertex(name = 'V_392',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_327_227,(0,0,2):C.UVGC_327_228,(0,0,1):C.UVGC_327_229})

V_393 = CTVertex(name = 'V_393',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_329_231,(0,0,2):C.UVGC_329_232,(0,0,1):C.UVGC_329_233})

V_394 = CTVertex(name = 'V_394',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_329_231,(0,0,2):C.UVGC_329_232,(0,0,1):C.UVGC_329_233})

V_395 = CTVertex(name = 'V_395',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_327_228,(0,0,2):C.UVGC_328_230,(0,0,1):C.UVGC_327_229})

V_396 = CTVertex(name = 'V_396',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.Xd1, P.Xu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_469_809,(0,0,6):C.UVGC_469_810,(0,0,8):C.UVGC_469_811,(0,0,10):C.UVGC_469_812,(0,0,1):C.UVGC_469_813,(0,0,3):C.UVGC_469_814,(0,0,5):C.UVGC_469_815,(0,0,7):C.UVGC_469_816,(0,0,9):C.UVGC_469_817,(0,0,2):C.UVGC_469_818,(0,0,4):C.UVGC_469_819})

V_397 = CTVertex(name = 'V_397',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.Xd2, P.Xu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_467_787,(0,0,4):C.UVGC_467_788,(0,0,8):C.UVGC_467_789,(0,0,10):C.UVGC_467_790,(0,0,1):C.UVGC_467_791,(0,0,3):C.UVGC_467_792,(0,0,5):C.UVGC_467_793,(0,0,7):C.UVGC_467_794,(0,0,9):C.UVGC_467_795,(0,0,2):C.UVGC_467_796,(0,0,6):C.UVGC_467_797})

V_398 = CTVertex(name = 'V_398',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.Xd1__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_469_809,(0,0,6):C.UVGC_469_810,(0,0,8):C.UVGC_469_811,(0,0,10):C.UVGC_469_812,(0,0,1):C.UVGC_469_813,(0,0,3):C.UVGC_469_814,(0,0,5):C.UVGC_469_815,(0,0,7):C.UVGC_469_816,(0,0,9):C.UVGC_469_817,(0,0,2):C.UVGC_469_818,(0,0,4):C.UVGC_469_819})

V_399 = CTVertex(name = 'V_399',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.Xd2__tilde__, P.Xu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_467_787,(0,0,4):C.UVGC_467_788,(0,0,8):C.UVGC_467_789,(0,0,10):C.UVGC_467_790,(0,0,1):C.UVGC_467_791,(0,0,3):C.UVGC_467_792,(0,0,5):C.UVGC_467_793,(0,0,7):C.UVGC_467_794,(0,0,9):C.UVGC_467_795,(0,0,2):C.UVGC_467_796,(0,0,6):C.UVGC_467_797})

V_400 = CTVertex(name = 'V_400',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.Xd1, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_468_798,(0,0,6):C.UVGC_468_799,(0,0,8):C.UVGC_468_800,(0,0,10):C.UVGC_468_801,(0,0,1):C.UVGC_468_802,(0,0,3):C.UVGC_468_803,(0,0,5):C.UVGC_468_804,(0,0,7):C.UVGC_468_805,(0,0,9):C.UVGC_468_806,(0,0,2):C.UVGC_468_807,(0,0,4):C.UVGC_468_808})

V_401 = CTVertex(name = 'V_401',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.Xd2, P.Xu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_466_776,(0,0,4):C.UVGC_466_777,(0,0,8):C.UVGC_466_778,(0,0,10):C.UVGC_466_779,(0,0,1):C.UVGC_466_780,(0,0,3):C.UVGC_466_781,(0,0,5):C.UVGC_466_782,(0,0,7):C.UVGC_466_783,(0,0,9):C.UVGC_466_784,(0,0,2):C.UVGC_466_785,(0,0,6):C.UVGC_466_786})

V_402 = CTVertex(name = 'V_402',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.Xd1__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_468_798,(0,0,6):C.UVGC_468_799,(0,0,8):C.UVGC_468_800,(0,0,10):C.UVGC_468_801,(0,0,1):C.UVGC_468_802,(0,0,3):C.UVGC_468_803,(0,0,5):C.UVGC_468_804,(0,0,7):C.UVGC_468_805,(0,0,9):C.UVGC_468_806,(0,0,2):C.UVGC_468_807,(0,0,4):C.UVGC_468_808})

V_403 = CTVertex(name = 'V_403',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.Xd2__tilde__, P.Xu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_466_776,(0,0,4):C.UVGC_466_777,(0,0,8):C.UVGC_466_778,(0,0,10):C.UVGC_466_779,(0,0,1):C.UVGC_466_780,(0,0,3):C.UVGC_466_781,(0,0,5):C.UVGC_466_782,(0,0,7):C.UVGC_466_783,(0,0,9):C.UVGC_466_784,(0,0,2):C.UVGC_466_785,(0,0,6):C.UVGC_466_786})

V_404 = CTVertex(name = 'V_404',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_260_57,(0,1,0):C.UVGC_374_510,(0,2,0):C.UVGC_374_510})

V_405 = CTVertex(name = 'V_405',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_260_57,(0,1,0):C.UVGC_412_572,(0,2,0):C.UVGC_412_572})

V_406 = CTVertex(name = 'V_406',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_260_57,(0,1,0):C.UVGC_426_598,(0,2,0):C.UVGC_426_598})

V_407 = CTVertex(name = 'V_407',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_258_55,(0,1,0):C.UVGC_366_490,(0,2,0):C.UVGC_366_490})

V_408 = CTVertex(name = 'V_408',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_258_55,(0,1,0):C.UVGC_382_518,(0,2,0):C.UVGC_382_518})

V_409 = CTVertex(name = 'V_409',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_258_55,(0,1,0):C.UVGC_398_546,(0,2,0):C.UVGC_398_546})

V_410 = CTVertex(name = 'V_410',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,2):C.UVGC_259_56,(0,1,0):C.UVGC_367_491,(0,1,1):C.UVGC_367_492,(0,1,3):C.UVGC_367_493,(0,1,4):C.UVGC_367_494,(0,1,5):C.UVGC_367_495,(0,1,6):C.UVGC_367_496,(0,1,7):C.UVGC_367_497,(0,1,8):C.UVGC_367_498,(0,1,9):C.UVGC_367_499,(0,1,10):C.UVGC_367_500,(0,1,11):C.UVGC_367_501,(0,1,12):C.UVGC_367_502,(0,1,2):C.UVGC_375_511,(0,2,0):C.UVGC_367_491,(0,2,1):C.UVGC_367_492,(0,2,3):C.UVGC_367_493,(0,2,4):C.UVGC_367_494,(0,2,5):C.UVGC_367_495,(0,2,6):C.UVGC_367_496,(0,2,7):C.UVGC_367_497,(0,2,8):C.UVGC_367_498,(0,2,9):C.UVGC_367_499,(0,2,10):C.UVGC_367_500,(0,2,11):C.UVGC_367_501,(0,2,12):C.UVGC_367_502,(0,2,2):C.UVGC_375_511})

V_411 = CTVertex(name = 'V_411',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,5):C.UVGC_259_56,(0,1,0):C.UVGC_367_491,(0,1,1):C.UVGC_367_492,(0,1,2):C.UVGC_367_493,(0,1,3):C.UVGC_367_494,(0,1,4):C.UVGC_367_495,(0,1,6):C.UVGC_367_496,(0,1,7):C.UVGC_367_497,(0,1,8):C.UVGC_367_498,(0,1,9):C.UVGC_367_499,(0,1,10):C.UVGC_367_500,(0,1,11):C.UVGC_367_501,(0,1,12):C.UVGC_367_502,(0,1,5):C.UVGC_413_573,(0,2,0):C.UVGC_367_491,(0,2,1):C.UVGC_367_492,(0,2,2):C.UVGC_367_493,(0,2,3):C.UVGC_367_494,(0,2,4):C.UVGC_367_495,(0,2,6):C.UVGC_367_496,(0,2,7):C.UVGC_367_497,(0,2,8):C.UVGC_367_498,(0,2,9):C.UVGC_367_499,(0,2,10):C.UVGC_367_500,(0,2,11):C.UVGC_367_501,(0,2,12):C.UVGC_367_502,(0,2,5):C.UVGC_413_573})

V_412 = CTVertex(name = 'V_412',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,5):C.UVGC_259_56,(0,1,0):C.UVGC_367_491,(0,1,1):C.UVGC_367_492,(0,1,2):C.UVGC_367_493,(0,1,3):C.UVGC_367_494,(0,1,4):C.UVGC_367_495,(0,1,6):C.UVGC_367_496,(0,1,7):C.UVGC_367_497,(0,1,8):C.UVGC_367_498,(0,1,9):C.UVGC_367_499,(0,1,10):C.UVGC_367_500,(0,1,11):C.UVGC_367_501,(0,1,12):C.UVGC_367_502,(0,1,5):C.UVGC_427_599,(0,2,0):C.UVGC_367_491,(0,2,1):C.UVGC_367_492,(0,2,2):C.UVGC_367_493,(0,2,3):C.UVGC_367_494,(0,2,4):C.UVGC_367_495,(0,2,6):C.UVGC_367_496,(0,2,7):C.UVGC_367_497,(0,2,8):C.UVGC_367_498,(0,2,9):C.UVGC_367_499,(0,2,10):C.UVGC_367_500,(0,2,11):C.UVGC_367_501,(0,2,12):C.UVGC_367_502,(0,2,5):C.UVGC_427_599})

V_413 = CTVertex(name = 'V_413',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,1):C.UVGC_259_56,(0,1,0):C.UVGC_367_491,(0,1,2):C.UVGC_367_492,(0,1,3):C.UVGC_367_493,(0,1,4):C.UVGC_367_494,(0,1,5):C.UVGC_367_495,(0,1,6):C.UVGC_367_496,(0,1,7):C.UVGC_367_497,(0,1,8):C.UVGC_367_498,(0,1,9):C.UVGC_367_499,(0,1,10):C.UVGC_367_500,(0,1,11):C.UVGC_367_501,(0,1,12):C.UVGC_367_502,(0,1,1):C.UVGC_367_503,(0,2,0):C.UVGC_367_491,(0,2,2):C.UVGC_367_492,(0,2,3):C.UVGC_367_493,(0,2,4):C.UVGC_367_494,(0,2,5):C.UVGC_367_495,(0,2,6):C.UVGC_367_496,(0,2,7):C.UVGC_367_497,(0,2,8):C.UVGC_367_498,(0,2,9):C.UVGC_367_499,(0,2,10):C.UVGC_367_500,(0,2,11):C.UVGC_367_501,(0,2,12):C.UVGC_367_502,(0,2,1):C.UVGC_367_503})

V_414 = CTVertex(name = 'V_414',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,3):C.UVGC_259_56,(0,1,0):C.UVGC_367_491,(0,1,1):C.UVGC_367_492,(0,1,2):C.UVGC_367_493,(0,1,4):C.UVGC_367_494,(0,1,5):C.UVGC_367_495,(0,1,6):C.UVGC_367_496,(0,1,7):C.UVGC_367_497,(0,1,8):C.UVGC_367_498,(0,1,9):C.UVGC_367_499,(0,1,10):C.UVGC_367_500,(0,1,11):C.UVGC_367_501,(0,1,12):C.UVGC_367_502,(0,1,3):C.UVGC_383_519,(0,2,0):C.UVGC_367_491,(0,2,1):C.UVGC_367_492,(0,2,2):C.UVGC_367_493,(0,2,4):C.UVGC_367_494,(0,2,5):C.UVGC_367_495,(0,2,6):C.UVGC_367_496,(0,2,7):C.UVGC_367_497,(0,2,8):C.UVGC_367_498,(0,2,9):C.UVGC_367_499,(0,2,10):C.UVGC_367_500,(0,2,11):C.UVGC_367_501,(0,2,12):C.UVGC_367_502,(0,2,3):C.UVGC_383_519})

V_415 = CTVertex(name = 'V_415',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,5):C.UVGC_259_56,(0,1,0):C.UVGC_367_491,(0,1,1):C.UVGC_367_492,(0,1,2):C.UVGC_367_493,(0,1,3):C.UVGC_367_494,(0,1,4):C.UVGC_367_495,(0,1,6):C.UVGC_367_496,(0,1,7):C.UVGC_367_497,(0,1,8):C.UVGC_367_498,(0,1,9):C.UVGC_367_499,(0,1,10):C.UVGC_367_500,(0,1,11):C.UVGC_367_501,(0,1,12):C.UVGC_367_502,(0,1,5):C.UVGC_399_547,(0,2,0):C.UVGC_367_491,(0,2,1):C.UVGC_367_492,(0,2,2):C.UVGC_367_493,(0,2,3):C.UVGC_367_494,(0,2,4):C.UVGC_367_495,(0,2,6):C.UVGC_367_496,(0,2,7):C.UVGC_367_497,(0,2,8):C.UVGC_367_498,(0,2,9):C.UVGC_367_499,(0,2,10):C.UVGC_367_500,(0,2,11):C.UVGC_367_501,(0,2,12):C.UVGC_367_502,(0,2,5):C.UVGC_399_547})

V_416 = CTVertex(name = 'V_416',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_385_521,(0,0,2):C.UVGC_385_522,(0,0,0):C.UVGC_385_523})

V_417 = CTVertex(name = 'V_417',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_401_549,(0,0,2):C.UVGC_401_550,(0,0,1):C.UVGC_401_551})

V_418 = CTVertex(name = 'V_418',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_415_575,(0,0,2):C.UVGC_415_576,(0,0,1):C.UVGC_415_577})

V_419 = CTVertex(name = 'V_419',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_429_601,(0,0,2):C.UVGC_429_602,(0,0,1):C.UVGC_429_603})

V_420 = CTVertex(name = 'V_420',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_430_604,(0,0,2):C.UVGC_430_605,(0,0,1):C.UVGC_430_606})

V_421 = CTVertex(name = 'V_421',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_422_588,(0,0,2):C.UVGC_422_589,(0,0,1):C.UVGC_422_590})

V_422 = CTVertex(name = 'V_422',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_392_534,(0,0,2):C.UVGC_392_535,(0,0,0):C.UVGC_392_536})

V_423 = CTVertex(name = 'V_423',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_439_623,(0,0,2):C.UVGC_439_624,(0,0,1):C.UVGC_439_625})

V_424 = CTVertex(name = 'V_424',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_408_562,(0,0,2):C.UVGC_408_563,(0,0,1):C.UVGC_408_564})

V_425 = CTVertex(name = 'V_425',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_442_632,(0,0,2):C.UVGC_442_633,(0,0,1):C.UVGC_442_634})

V_426 = CTVertex(name = 'V_426',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_377_513,(0,1,0):C.UVGC_378_514})

V_427 = CTVertex(name = 'V_427',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_416_578,(0,1,0):C.UVGC_417_579})

V_428 = CTVertex(name = 'V_428',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_431_607,(0,1,0):C.UVGC_432_608})

V_429 = CTVertex(name = 'V_429',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_369_505,(0,1,0):C.UVGC_370_506})

V_430 = CTVertex(name = 'V_430',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_386_524,(0,1,0):C.UVGC_387_525})

V_431 = CTVertex(name = 'V_431',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_402_552,(0,1,0):C.UVGC_403_553})

V_432 = CTVertex(name = 'V_432',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_368_504,(0,2,0):C.UVGC_368_504,(0,1,0):C.UVGC_365_489,(0,3,0):C.UVGC_365_489})

V_433 = CTVertex(name = 'V_433',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_376_512,(0,2,0):C.UVGC_376_512,(0,1,0):C.UVGC_373_509,(0,3,0):C.UVGC_373_509})

V_434 = CTVertex(name = 'V_434',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_384_520,(0,2,0):C.UVGC_384_520,(0,1,0):C.UVGC_381_517,(0,3,0):C.UVGC_381_517})

V_435 = CTVertex(name = 'V_435',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_400_548,(0,2,0):C.UVGC_400_548,(0,1,0):C.UVGC_397_545,(0,3,0):C.UVGC_397_545})

V_436 = CTVertex(name = 'V_436',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_414_574,(0,2,0):C.UVGC_414_574,(0,1,0):C.UVGC_411_571,(0,3,0):C.UVGC_411_571})

V_437 = CTVertex(name = 'V_437',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_428_600,(0,2,0):C.UVGC_428_600,(0,1,0):C.UVGC_425_597,(0,3,0):C.UVGC_425_597})

V_438 = CTVertex(name = 'V_438',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xd1] ] ],
                 couplings = {(0,0,0):C.UVGC_395_543,(0,1,0):C.UVGC_269_64})

V_439 = CTVertex(name = 'V_439',
                 type = 'UV',
                 particles = [ P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xu1] ] ],
                 couplings = {(0,0,0):C.UVGC_445_641,(0,1,0):C.UVGC_281_76})

V_440 = CTVertex(name = 'V_440',
                 type = 'UV',
                 particles = [ P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xd2] ] ],
                 couplings = {(0,0,0):C.UVGC_396_544,(0,1,0):C.UVGC_275_69})

V_441 = CTVertex(name = 'V_441',
                 type = 'UV',
                 particles = [ P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_460_762,(0,1,0):C.UVGC_297_139})

V_442 = CTVertex(name = 'V_442',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_447_652,(0,0,1):C.UVGC_447_653,(0,0,2):C.UVGC_447_654,(0,0,3):C.UVGC_447_655,(0,0,4):C.UVGC_447_656,(0,0,5):C.UVGC_447_657,(0,0,6):C.UVGC_447_658,(0,0,7):C.UVGC_447_659,(0,0,8):C.UVGC_447_660,(0,0,9):C.UVGC_447_661,(0,0,10):C.UVGC_447_662,(0,0,11):C.UVGC_447_663,(0,1,8):C.UVGC_243_5,(0,1,9):C.UVGC_243_6,(0,1,10):C.UVGC_243_7,(0,1,11):C.UVGC_243_8,(0,2,0):C.UVGC_446_642,(0,2,1):C.UVGC_446_643,(0,2,2):C.UVGC_446_644,(0,2,5):C.UVGC_446_645,(0,2,6):C.UVGC_446_646,(0,2,7):C.UVGC_446_647,(0,2,8):C.UVGC_446_648,(0,2,9):C.UVGC_446_649,(0,2,10):C.UVGC_446_650,(0,2,11):C.UVGC_446_651})

V_443 = CTVertex(name = 'V_443',
                 type = 'UV',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_257_51,(0,0,1):C.UVGC_257_52,(0,0,2):C.UVGC_257_53,(0,0,3):C.UVGC_257_54})

V_444 = CTVertex(name = 'V_444',
                 type = 'UV',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.Xd1], [P.Xd2] ], [ [P.Xu1], [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_247_17,(0,0,1):C.UVGC_247_18,(0,1,0):C.UVGC_247_17,(0,1,1):C.UVGC_247_18,(0,2,0):C.UVGC_247_17,(0,2,1):C.UVGC_247_18})

V_445 = CTVertex(name = 'V_445',
                 type = 'UV',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_255_43,(0,0,1):C.UVGC_255_44,(0,0,2):C.UVGC_255_45,(0,0,3):C.UVGC_255_46,(0,1,0):C.UVGC_255_43,(0,1,1):C.UVGC_255_44,(0,1,2):C.UVGC_255_45,(0,1,3):C.UVGC_255_46,(0,2,0):C.UVGC_255_43,(0,2,1):C.UVGC_255_44,(0,2,2):C.UVGC_255_45,(0,2,3):C.UVGC_255_46})

V_446 = CTVertex(name = 'V_446',
                 type = 'UV',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd1, P.Xd2] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu1, P.Xu2] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_317_180,(0,0,2):C.UVGC_317_181,(0,0,3):C.UVGC_317_182,(0,0,5):C.UVGC_317_183,(0,0,1):C.UVGC_317_184,(0,0,4):C.UVGC_317_185,(0,1,0):C.UVGC_317_180,(0,1,2):C.UVGC_317_181,(0,1,3):C.UVGC_317_182,(0,1,5):C.UVGC_317_183,(0,1,1):C.UVGC_317_184,(0,1,4):C.UVGC_317_185,(0,2,0):C.UVGC_316_174,(0,2,2):C.UVGC_316_175,(0,2,3):C.UVGC_316_176,(0,2,5):C.UVGC_316_177,(0,2,1):C.UVGC_316_178,(0,2,4):C.UVGC_316_179})

V_447 = CTVertex(name = 'V_447',
                 type = 'UV',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd1, P.Xu1] ], [ [P.Xd1, P.Xu2] ], [ [P.Xd2] ], [ [P.Xd2, P.Xu1] ], [ [P.Xd2, P.Xu2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,1):C.UVGC_315_170,(0,0,2):C.UVGC_315_171,(0,0,4):C.UVGC_315_172,(0,0,5):C.UVGC_315_173,(0,1,1):C.UVGC_315_170,(0,1,2):C.UVGC_315_171,(0,1,4):C.UVGC_315_172,(0,1,5):C.UVGC_315_173,(0,2,0):C.UVGC_314_162,(0,2,3):C.UVGC_314_163,(0,2,6):C.UVGC_314_164,(0,2,7):C.UVGC_314_165,(0,2,1):C.UVGC_314_166,(0,2,2):C.UVGC_314_167,(0,2,4):C.UVGC_314_168,(0,2,5):C.UVGC_314_169})

V_448 = CTVertex(name = 'V_448',
                 type = 'UV',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.Xd1], [P.Xd2] ], [ [P.Xu1], [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_248_19,(0,0,1):C.UVGC_248_20,(0,1,0):C.UVGC_248_19,(0,1,1):C.UVGC_248_20,(0,2,0):C.UVGC_248_19,(0,2,1):C.UVGC_248_20})

V_449 = CTVertex(name = 'V_449',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_256_47,(0,0,1):C.UVGC_256_48,(0,0,2):C.UVGC_256_49,(0,0,3):C.UVGC_256_50,(0,1,0):C.UVGC_256_47,(0,1,1):C.UVGC_256_48,(0,1,2):C.UVGC_256_49,(0,1,3):C.UVGC_256_50,(0,2,0):C.UVGC_256_47,(0,2,1):C.UVGC_256_48,(0,2,2):C.UVGC_256_49,(0,2,3):C.UVGC_256_50})

V_450 = CTVertex(name = 'V_450',
                 type = 'UV',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_245_13,(0,0,1):C.UVGC_245_14,(0,0,2):C.UVGC_245_15,(0,0,3):C.UVGC_245_16})

V_451 = CTVertex(name = 'V_451',
                 type = 'UV',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_245_13,(0,0,1):C.UVGC_245_14,(0,0,2):C.UVGC_245_15,(0,0,3):C.UVGC_245_16})

V_452 = CTVertex(name = 'V_452',
                 type = 'UV',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.Xd1] ], [ [P.Xd2] ], [ [P.Xu1] ], [ [P.Xu2] ] ],
                 couplings = {(0,0,0):C.UVGC_245_13,(0,0,1):C.UVGC_245_14,(0,0,2):C.UVGC_245_15,(0,0,3):C.UVGC_245_16})

V_453 = CTVertex(name = 'V_453',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1__tilde__, P.Xd1, P.Xd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1] ], [ [P.g] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_330_234,(1,0,0):C.UVGC_330_235,(1,0,3):C.UVGC_330_236,(1,0,5):C.UVGC_330_237,(1,0,1):C.UVGC_330_238,(1,0,4):C.UVGC_330_239,(0,0,2):C.UVGC_330_234,(0,0,0):C.UVGC_330_235,(0,0,3):C.UVGC_330_236,(0,0,5):C.UVGC_330_237,(0,0,1):C.UVGC_330_238,(0,0,4):C.UVGC_330_239})

V_454 = CTVertex(name = 'V_454',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1] ], [ [P.a, P.g, P.Xd1, P.Xu1] ], [ [P.a, P.g, P.Xu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.UVGC_341_304,(1,0,0):C.UVGC_341_305,(1,0,5):C.UVGC_341_306,(1,0,9):C.UVGC_341_307,(1,0,13):C.UVGC_341_308,(1,0,15):C.UVGC_341_309,(1,0,1):C.UVGC_341_310,(1,0,3):C.UVGC_341_311,(1,0,6):C.UVGC_341_312,(1,0,8):C.UVGC_341_313,(1,0,10):C.UVGC_341_314,(1,0,12):C.UVGC_341_315,(1,0,14):C.UVGC_341_316,(1,0,2):C.UVGC_341_317,(1,0,7):C.UVGC_341_318,(1,0,11):C.UVGC_341_319,(0,0,4):C.UVGC_340_288,(0,0,0):C.UVGC_340_289,(0,0,5):C.UVGC_340_290,(0,0,9):C.UVGC_340_291,(0,0,13):C.UVGC_340_292,(0,0,15):C.UVGC_340_293,(0,0,1):C.UVGC_340_294,(0,0,3):C.UVGC_340_295,(0,0,6):C.UVGC_340_296,(0,0,8):C.UVGC_340_297,(0,0,10):C.UVGC_340_298,(0,0,12):C.UVGC_340_299,(0,0,14):C.UVGC_340_300,(0,0,2):C.UVGC_340_301,(0,0,7):C.UVGC_340_302,(0,0,11):C.UVGC_340_303})

V_455 = CTVertex(name = 'V_455',
                 type = 'UV',
                 particles = [ P.Xu1__tilde__, P.Xu1__tilde__, P.Xu1, P.Xu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xu1] ], [ [P.g] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_332_242,(1,0,0):C.UVGC_332_243,(1,0,3):C.UVGC_332_244,(1,0,5):C.UVGC_332_245,(1,0,1):C.UVGC_332_246,(1,0,4):C.UVGC_332_247,(0,0,2):C.UVGC_332_242,(0,0,0):C.UVGC_332_243,(0,0,3):C.UVGC_332_244,(0,0,5):C.UVGC_332_245,(0,0,1):C.UVGC_332_246,(0,0,4):C.UVGC_332_247})

V_456 = CTVertex(name = 'V_456',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1__tilde__, P.Xd1, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_336_262,(1,0,1):C.UVGC_336_263,(1,0,2):C.UVGC_336_264,(1,0,0):C.UVGC_336_265,(0,0,3):C.UVGC_336_262,(0,0,1):C.UVGC_336_263,(0,0,2):C.UVGC_336_264,(0,0,0):C.UVGC_336_265})

V_457 = CTVertex(name = 'V_457',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu1, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_357_435,(1,0,8):C.UVGC_357_436,(1,0,1):C.UVGC_357_437,(1,0,4):C.UVGC_357_438,(1,0,6):C.UVGC_357_439,(1,0,7):C.UVGC_357_440,(1,0,2):C.UVGC_357_441,(1,0,3):C.UVGC_357_442,(1,0,5):C.UVGC_357_443,(0,0,0):C.UVGC_356_426,(0,0,8):C.UVGC_356_427,(0,0,1):C.UVGC_356_428,(0,0,4):C.UVGC_356_429,(0,0,6):C.UVGC_356_430,(0,0,7):C.UVGC_356_431,(0,0,2):C.UVGC_356_432,(0,0,3):C.UVGC_356_433,(0,0,5):C.UVGC_356_434})

V_458 = CTVertex(name = 'V_458',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1__tilde__, P.Xd2, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_335_259,(1,0,1):C.UVGC_335_260,(1,0,0):C.UVGC_335_261,(0,0,2):C.UVGC_335_259,(0,0,1):C.UVGC_335_260,(0,0,0):C.UVGC_335_261})

V_459 = CTVertex(name = 'V_459',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xd1, P.Xd2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_336_262,(1,0,1):C.UVGC_336_263,(1,0,2):C.UVGC_336_264,(1,0,0):C.UVGC_336_265,(0,0,3):C.UVGC_336_262,(0,0,1):C.UVGC_336_263,(0,0,2):C.UVGC_336_264,(0,0,0):C.UVGC_336_265})

V_460 = CTVertex(name = 'V_460',
                 type = 'UV',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu1, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_357_435,(1,0,8):C.UVGC_357_436,(1,0,1):C.UVGC_357_437,(1,0,4):C.UVGC_357_438,(1,0,6):C.UVGC_357_439,(1,0,7):C.UVGC_357_440,(1,0,2):C.UVGC_357_441,(1,0,3):C.UVGC_357_442,(1,0,5):C.UVGC_357_443,(0,0,0):C.UVGC_356_426,(0,0,8):C.UVGC_356_427,(0,0,1):C.UVGC_356_428,(0,0,4):C.UVGC_356_429,(0,0,6):C.UVGC_356_430,(0,0,7):C.UVGC_356_431,(0,0,2):C.UVGC_356_432,(0,0,3):C.UVGC_356_433,(0,0,5):C.UVGC_356_434})

V_461 = CTVertex(name = 'V_461',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1], [P.a, P.g, P.Xd2] ], [ [P.a, P.g, P.Xd1, P.Xd2] ], [ [P.g] ], [ [P.g, P.Xd1], [P.g, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2] ], [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_339_279,(1,0,0):C.UVGC_339_280,(1,0,4):C.UVGC_339_281,(1,0,8):C.UVGC_339_282,(1,0,1):C.UVGC_339_283,(1,0,5):C.UVGC_339_284,(1,0,7):C.UVGC_339_285,(1,0,2):C.UVGC_339_286,(1,0,6):C.UVGC_339_287,(0,0,3):C.UVGC_338_270,(0,0,0):C.UVGC_338_271,(0,0,4):C.UVGC_338_272,(0,0,8):C.UVGC_338_273,(0,0,1):C.UVGC_338_274,(0,0,5):C.UVGC_338_275,(0,0,7):C.UVGC_338_276,(0,0,2):C.UVGC_338_277,(0,0,6):C.UVGC_338_278})

V_462 = CTVertex(name = 'V_462',
                 type = 'UV',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd2] ], [ [P.a, P.g, P.Xd2, P.Xu1] ], [ [P.a, P.g, P.Xu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu1] ], [ [P.g, P.Xd2, P.Xu1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.UVGC_341_304,(1,0,0):C.UVGC_341_305,(1,0,5):C.UVGC_359_452,(1,0,9):C.UVGC_341_307,(1,0,13):C.UVGC_341_308,(1,0,15):C.UVGC_359_453,(1,0,1):C.UVGC_341_310,(1,0,3):C.UVGC_341_311,(1,0,6):C.UVGC_359_454,(1,0,8):C.UVGC_359_455,(1,0,10):C.UVGC_341_314,(1,0,12):C.UVGC_359_456,(1,0,14):C.UVGC_359_457,(1,0,2):C.UVGC_341_317,(1,0,7):C.UVGC_359_458,(1,0,11):C.UVGC_359_459,(0,0,4):C.UVGC_340_288,(0,0,0):C.UVGC_340_289,(0,0,5):C.UVGC_358_444,(0,0,9):C.UVGC_340_291,(0,0,13):C.UVGC_340_292,(0,0,15):C.UVGC_358_445,(0,0,1):C.UVGC_340_294,(0,0,3):C.UVGC_340_295,(0,0,6):C.UVGC_358_446,(0,0,8):C.UVGC_358_447,(0,0,10):C.UVGC_340_298,(0,0,12):C.UVGC_358_448,(0,0,14):C.UVGC_358_449,(0,0,2):C.UVGC_340_301,(0,0,7):C.UVGC_358_450,(0,0,11):C.UVGC_358_451})

V_463 = CTVertex(name = 'V_463',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd2__tilde__, P.Xd2, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_337_266,(1,0,1):C.UVGC_337_267,(1,0,2):C.UVGC_337_268,(1,0,0):C.UVGC_337_269,(0,0,3):C.UVGC_337_266,(0,0,1):C.UVGC_337_267,(0,0,2):C.UVGC_337_268,(0,0,0):C.UVGC_337_269})

V_464 = CTVertex(name = 'V_464',
                 type = 'UV',
                 particles = [ P.Xd1, P.Xd1, P.Xd2__tilde__, P.Xd2__tilde__ ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_335_259,(1,0,1):C.UVGC_335_260,(1,0,0):C.UVGC_335_261,(0,0,2):C.UVGC_335_259,(0,0,1):C.UVGC_335_260,(0,0,0):C.UVGC_335_261})

V_465 = CTVertex(name = 'V_465',
                 type = 'UV',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xd2__tilde__, P.Xd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xd1, P.Xd2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_337_266,(1,0,1):C.UVGC_337_267,(1,0,2):C.UVGC_337_268,(1,0,0):C.UVGC_337_269,(0,0,3):C.UVGC_337_266,(0,0,1):C.UVGC_337_267,(0,0,2):C.UVGC_337_268,(0,0,0):C.UVGC_337_269})

V_466 = CTVertex(name = 'V_466',
                 type = 'UV',
                 particles = [ P.Xd2__tilde__, P.Xd2__tilde__, P.Xd2, P.Xd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd2] ], [ [P.g] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_330_234,(1,0,0):C.UVGC_330_235,(1,0,3):C.UVGC_330_236,(1,0,5):C.UVGC_331_240,(1,0,1):C.UVGC_330_238,(1,0,4):C.UVGC_331_241,(0,0,2):C.UVGC_330_234,(0,0,0):C.UVGC_330_235,(0,0,3):C.UVGC_330_236,(0,0,5):C.UVGC_331_240,(0,0,1):C.UVGC_330_238,(0,0,4):C.UVGC_331_241})

V_467 = CTVertex(name = 'V_467',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd1, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_343_329,(1,0,8):C.UVGC_343_330,(1,0,1):C.UVGC_343_331,(1,0,3):C.UVGC_343_332,(1,0,6):C.UVGC_343_333,(1,0,7):C.UVGC_343_334,(1,0,2):C.UVGC_343_335,(1,0,4):C.UVGC_343_336,(1,0,5):C.UVGC_343_337,(0,0,0):C.UVGC_342_320,(0,0,8):C.UVGC_342_321,(0,0,1):C.UVGC_342_322,(0,0,3):C.UVGC_342_323,(0,0,6):C.UVGC_342_324,(0,0,7):C.UVGC_342_325,(0,0,2):C.UVGC_342_326,(0,0,4):C.UVGC_342_327,(0,0,5):C.UVGC_342_328})

V_468 = CTVertex(name = 'V_468',
                 type = 'UV',
                 particles = [ P.Xu1__tilde__, P.Xu1__tilde__, P.Xu1, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_361_463,(1,0,1):C.UVGC_361_464,(1,0,2):C.UVGC_361_465,(1,0,0):C.UVGC_361_466,(0,0,3):C.UVGC_361_463,(0,0,1):C.UVGC_361_464,(0,0,2):C.UVGC_361_465,(0,0,0):C.UVGC_361_466})

V_469 = CTVertex(name = 'V_469',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_352_398,(1,0,9):C.UVGC_352_399,(1,0,1):C.UVGC_352_400,(1,0,4):C.UVGC_352_401,(1,0,7):C.UVGC_352_402,(1,0,8):C.UVGC_352_403,(1,0,2):C.UVGC_352_404,(1,0,3):C.UVGC_352_405,(1,0,5):C.UVGC_352_406,(1,0,6):C.UVGC_352_407,(0,0,0):C.UVGC_350_388,(0,0,9):C.UVGC_350_389,(0,0,1):C.UVGC_350_390,(0,0,4):C.UVGC_350_391,(0,0,7):C.UVGC_350_392,(0,0,8):C.UVGC_350_393,(0,0,2):C.UVGC_350_394,(0,0,3):C.UVGC_350_395,(0,0,5):C.UVGC_350_396,(0,0,6):C.UVGC_350_397})

V_470 = CTVertex(name = 'V_470',
                 type = 'UV',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_352_398,(1,0,9):C.UVGC_352_399,(1,0,1):C.UVGC_352_400,(1,0,4):C.UVGC_352_401,(1,0,7):C.UVGC_352_402,(1,0,8):C.UVGC_352_403,(1,0,2):C.UVGC_352_404,(1,0,3):C.UVGC_352_405,(1,0,5):C.UVGC_352_406,(1,0,6):C.UVGC_352_407,(0,0,0):C.UVGC_350_388,(0,0,9):C.UVGC_350_389,(0,0,1):C.UVGC_350_390,(0,0,4):C.UVGC_350_391,(0,0,7):C.UVGC_350_392,(0,0,8):C.UVGC_350_393,(0,0,2):C.UVGC_350_394,(0,0,3):C.UVGC_350_395,(0,0,5):C.UVGC_350_396,(0,0,6):C.UVGC_350_397})

V_471 = CTVertex(name = 'V_471',
                 type = 'UV',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu1__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_355_417,(1,0,8):C.UVGC_355_418,(1,0,1):C.UVGC_355_419,(1,0,3):C.UVGC_355_420,(1,0,6):C.UVGC_355_421,(1,0,7):C.UVGC_355_422,(1,0,2):C.UVGC_355_423,(1,0,4):C.UVGC_355_424,(1,0,5):C.UVGC_355_425,(0,0,0):C.UVGC_354_408,(0,0,8):C.UVGC_354_409,(0,0,1):C.UVGC_354_410,(0,0,3):C.UVGC_354_411,(0,0,6):C.UVGC_354_412,(0,0,7):C.UVGC_354_413,(0,0,2):C.UVGC_354_414,(0,0,4):C.UVGC_354_415,(0,0,5):C.UVGC_354_416})

V_472 = CTVertex(name = 'V_472',
                 type = 'UV',
                 particles = [ P.Xu1__tilde__, P.Xu1__tilde__, P.Xu2, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_360_460,(1,0,1):C.UVGC_360_461,(1,0,0):C.UVGC_360_462,(0,0,2):C.UVGC_360_460,(0,0,1):C.UVGC_360_461,(0,0,0):C.UVGC_360_462})

V_473 = CTVertex(name = 'V_473',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd1, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_343_329,(1,0,8):C.UVGC_343_330,(1,0,1):C.UVGC_343_331,(1,0,3):C.UVGC_343_332,(1,0,6):C.UVGC_343_333,(1,0,7):C.UVGC_343_334,(1,0,2):C.UVGC_343_335,(1,0,4):C.UVGC_343_336,(1,0,5):C.UVGC_343_337,(0,0,0):C.UVGC_342_320,(0,0,8):C.UVGC_342_321,(0,0,1):C.UVGC_342_322,(0,0,3):C.UVGC_342_323,(0,0,6):C.UVGC_342_324,(0,0,7):C.UVGC_342_325,(0,0,2):C.UVGC_342_326,(0,0,4):C.UVGC_342_327,(0,0,5):C.UVGC_342_328})

V_474 = CTVertex(name = 'V_474',
                 type = 'UV',
                 particles = [ P.Xu1__tilde__, P.Xu1, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_361_463,(1,0,1):C.UVGC_361_464,(1,0,2):C.UVGC_361_465,(1,0,0):C.UVGC_361_466,(0,0,3):C.UVGC_361_463,(0,0,1):C.UVGC_361_464,(0,0,2):C.UVGC_361_465,(0,0,0):C.UVGC_361_466})

V_475 = CTVertex(name = 'V_475',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu1] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_352_398,(1,0,9):C.UVGC_352_399,(1,0,1):C.UVGC_352_400,(1,0,4):C.UVGC_352_401,(1,0,7):C.UVGC_352_402,(1,0,8):C.UVGC_352_403,(1,0,2):C.UVGC_352_404,(1,0,3):C.UVGC_352_405,(1,0,5):C.UVGC_352_406,(1,0,6):C.UVGC_352_407,(0,0,0):C.UVGC_350_388,(0,0,9):C.UVGC_350_389,(0,0,1):C.UVGC_350_390,(0,0,4):C.UVGC_350_391,(0,0,7):C.UVGC_350_392,(0,0,8):C.UVGC_350_393,(0,0,2):C.UVGC_350_394,(0,0,3):C.UVGC_350_395,(0,0,5):C.UVGC_350_396,(0,0,6):C.UVGC_350_397})

V_476 = CTVertex(name = 'V_476',
                 type = 'UV',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu1, P.Z], [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_352_398,(1,0,9):C.UVGC_352_399,(1,0,1):C.UVGC_352_400,(1,0,4):C.UVGC_352_401,(1,0,7):C.UVGC_352_402,(1,0,8):C.UVGC_352_403,(1,0,2):C.UVGC_352_404,(1,0,3):C.UVGC_352_405,(1,0,5):C.UVGC_352_406,(1,0,6):C.UVGC_352_407,(0,0,0):C.UVGC_350_388,(0,0,9):C.UVGC_350_389,(0,0,1):C.UVGC_350_390,(0,0,4):C.UVGC_350_391,(0,0,7):C.UVGC_350_392,(0,0,8):C.UVGC_350_393,(0,0,2):C.UVGC_350_394,(0,0,3):C.UVGC_350_395,(0,0,5):C.UVGC_350_396,(0,0,6):C.UVGC_350_397})

V_477 = CTVertex(name = 'V_477',
                 type = 'UV',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu1, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu1], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1], [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu1, P.Xu2] ], [ [P.g, P.Xd2, P.Xu1, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_355_417,(1,0,8):C.UVGC_355_418,(1,0,1):C.UVGC_355_419,(1,0,3):C.UVGC_355_420,(1,0,6):C.UVGC_355_421,(1,0,7):C.UVGC_355_422,(1,0,2):C.UVGC_355_423,(1,0,4):C.UVGC_355_424,(1,0,5):C.UVGC_355_425,(0,0,0):C.UVGC_354_408,(0,0,8):C.UVGC_354_409,(0,0,1):C.UVGC_354_410,(0,0,3):C.UVGC_354_411,(0,0,6):C.UVGC_354_412,(0,0,7):C.UVGC_354_413,(0,0,2):C.UVGC_354_414,(0,0,4):C.UVGC_354_415,(0,0,5):C.UVGC_354_416})

V_478 = CTVertex(name = 'V_478',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd1, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd1] ], [ [P.a, P.g, P.Xd1, P.Xu2] ], [ [P.a, P.g, P.Xu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd1] ], [ [P.g, P.Xd1, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z] ], [ [P.g, P.Xu2] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.UVGC_341_304,(1,0,0):C.UVGC_341_305,(1,0,5):C.UVGC_345_346,(1,0,9):C.UVGC_341_307,(1,0,13):C.UVGC_341_308,(1,0,15):C.UVGC_345_347,(1,0,1):C.UVGC_341_310,(1,0,3):C.UVGC_341_311,(1,0,6):C.UVGC_345_348,(1,0,8):C.UVGC_345_349,(1,0,10):C.UVGC_341_314,(1,0,12):C.UVGC_345_350,(1,0,14):C.UVGC_345_351,(1,0,2):C.UVGC_341_317,(1,0,7):C.UVGC_345_352,(1,0,11):C.UVGC_345_353,(0,0,4):C.UVGC_340_288,(0,0,0):C.UVGC_340_289,(0,0,5):C.UVGC_344_338,(0,0,9):C.UVGC_340_291,(0,0,13):C.UVGC_340_292,(0,0,15):C.UVGC_344_339,(0,0,1):C.UVGC_340_294,(0,0,3):C.UVGC_340_295,(0,0,6):C.UVGC_344_340,(0,0,8):C.UVGC_344_341,(0,0,10):C.UVGC_340_298,(0,0,12):C.UVGC_344_342,(0,0,14):C.UVGC_344_343,(0,0,2):C.UVGC_340_301,(0,0,7):C.UVGC_344_344,(0,0,11):C.UVGC_344_345})

V_479 = CTVertex(name = 'V_479',
                 type = 'UV',
                 particles = [ P.Xu1__tilde__, P.Xu1, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xu1], [P.a, P.g, P.Xu2] ], [ [P.a, P.g, P.Xu1, P.Xu2] ], [ [P.g] ], [ [P.g, P.Xu1], [P.g, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2] ], [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_364_480,(1,0,0):C.UVGC_364_481,(1,0,4):C.UVGC_364_482,(1,0,8):C.UVGC_364_483,(1,0,1):C.UVGC_364_484,(1,0,5):C.UVGC_364_485,(1,0,7):C.UVGC_364_486,(1,0,2):C.UVGC_364_487,(1,0,6):C.UVGC_364_488,(0,0,3):C.UVGC_363_471,(0,0,0):C.UVGC_363_472,(0,0,4):C.UVGC_363_473,(0,0,8):C.UVGC_363_474,(0,0,1):C.UVGC_363_475,(0,0,5):C.UVGC_363_476,(0,0,7):C.UVGC_363_477,(0,0,2):C.UVGC_363_478,(0,0,6):C.UVGC_363_479})

V_480 = CTVertex(name = 'V_480',
                 type = 'UV',
                 particles = [ P.Xd1__tilde__, P.Xd2, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_347_363,(1,0,8):C.UVGC_347_364,(1,0,1):C.UVGC_347_365,(1,0,4):C.UVGC_347_366,(1,0,6):C.UVGC_347_367,(1,0,7):C.UVGC_347_368,(1,0,2):C.UVGC_347_369,(1,0,3):C.UVGC_347_370,(1,0,5):C.UVGC_347_371,(0,0,0):C.UVGC_346_354,(0,0,8):C.UVGC_346_355,(0,0,1):C.UVGC_346_356,(0,0,4):C.UVGC_346_357,(0,0,6):C.UVGC_346_358,(0,0,7):C.UVGC_346_359,(0,0,2):C.UVGC_346_360,(0,0,3):C.UVGC_346_361,(0,0,5):C.UVGC_346_362})

V_481 = CTVertex(name = 'V_481',
                 type = 'UV',
                 particles = [ P.Xd1, P.Xd2__tilde__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd1], [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd1, P.Xu2], [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd1, P.Xu2, P.Z], [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd1, P.Z], [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,0):C.UVGC_347_363,(1,0,8):C.UVGC_347_364,(1,0,1):C.UVGC_347_365,(1,0,4):C.UVGC_347_366,(1,0,6):C.UVGC_347_367,(1,0,7):C.UVGC_347_368,(1,0,2):C.UVGC_347_369,(1,0,3):C.UVGC_347_370,(1,0,5):C.UVGC_347_371,(0,0,0):C.UVGC_346_354,(0,0,8):C.UVGC_346_355,(0,0,1):C.UVGC_346_356,(0,0,4):C.UVGC_346_357,(0,0,6):C.UVGC_346_358,(0,0,7):C.UVGC_346_359,(0,0,2):C.UVGC_346_360,(0,0,3):C.UVGC_346_361,(0,0,5):C.UVGC_346_362})

V_482 = CTVertex(name = 'V_482',
                 type = 'UV',
                 particles = [ P.Xd2__tilde__, P.Xd2, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xd2] ], [ [P.a, P.g, P.Xd2, P.Xu2] ], [ [P.a, P.g, P.Xu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.Xd2] ], [ [P.g, P.W__plus__, P.Xd2, P.Xu2] ], [ [P.g, P.W__plus__, P.Xu2] ], [ [P.g, P.Xd2] ], [ [P.g, P.Xd2, P.Xu2] ], [ [P.g, P.Xd2, P.Xu2, P.Z] ], [ [P.g, P.Xd2, P.Z] ], [ [P.g, P.Xu2] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,4):C.UVGC_341_304,(1,0,0):C.UVGC_341_305,(1,0,5):C.UVGC_349_380,(1,0,9):C.UVGC_341_307,(1,0,13):C.UVGC_341_308,(1,0,15):C.UVGC_349_381,(1,0,1):C.UVGC_341_310,(1,0,3):C.UVGC_341_311,(1,0,6):C.UVGC_349_382,(1,0,8):C.UVGC_349_383,(1,0,10):C.UVGC_341_314,(1,0,12):C.UVGC_349_384,(1,0,14):C.UVGC_349_385,(1,0,2):C.UVGC_341_317,(1,0,7):C.UVGC_349_386,(1,0,11):C.UVGC_349_387,(0,0,4):C.UVGC_340_288,(0,0,0):C.UVGC_340_289,(0,0,5):C.UVGC_348_372,(0,0,9):C.UVGC_340_291,(0,0,13):C.UVGC_340_292,(0,0,15):C.UVGC_348_373,(0,0,1):C.UVGC_340_294,(0,0,3):C.UVGC_340_295,(0,0,6):C.UVGC_348_374,(0,0,8):C.UVGC_348_375,(0,0,10):C.UVGC_340_298,(0,0,12):C.UVGC_348_376,(0,0,14):C.UVGC_348_377,(0,0,2):C.UVGC_340_301,(0,0,7):C.UVGC_348_378,(0,0,11):C.UVGC_348_379})

V_483 = CTVertex(name = 'V_483',
                 type = 'UV',
                 particles = [ P.Xu1__tilde__, P.Xu2__tilde__, P.Xu2, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_362_467,(1,0,1):C.UVGC_362_468,(1,0,2):C.UVGC_362_469,(1,0,0):C.UVGC_362_470,(0,0,3):C.UVGC_362_467,(0,0,1):C.UVGC_362_468,(0,0,2):C.UVGC_362_469,(0,0,0):C.UVGC_362_470})

V_484 = CTVertex(name = 'V_484',
                 type = 'UV',
                 particles = [ P.Xu1, P.Xu1, P.Xu2__tilde__, P.Xu2__tilde__ ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z], [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_360_460,(1,0,1):C.UVGC_360_461,(1,0,0):C.UVGC_360_462,(0,0,2):C.UVGC_360_460,(0,0,1):C.UVGC_360_461,(0,0,0):C.UVGC_360_462})

V_485 = CTVertex(name = 'V_485',
                 type = 'UV',
                 particles = [ P.Xu1, P.Xu2__tilde__, P.Xu2__tilde__, P.Xu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.Xu1, P.Xu2, P.Z] ], [ [P.g, P.Xu1, P.Z] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_362_467,(1,0,1):C.UVGC_362_468,(1,0,2):C.UVGC_362_469,(1,0,0):C.UVGC_362_470,(0,0,3):C.UVGC_362_467,(0,0,1):C.UVGC_362_468,(0,0,2):C.UVGC_362_469,(0,0,0):C.UVGC_362_470})

V_486 = CTVertex(name = 'V_486',
                 type = 'UV',
                 particles = [ P.Xu2__tilde__, P.Xu2__tilde__, P.Xu2, P.Xu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.Xu2] ], [ [P.g] ], [ [P.g, P.Xu2] ], [ [P.g, P.Xu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_332_242,(1,0,0):C.UVGC_332_243,(1,0,3):C.UVGC_332_244,(1,0,5):C.UVGC_333_248,(1,0,1):C.UVGC_332_246,(1,0,4):C.UVGC_333_249,(0,0,2):C.UVGC_332_242,(0,0,0):C.UVGC_332_243,(0,0,3):C.UVGC_332_244,(0,0,5):C.UVGC_333_248,(0,0,1):C.UVGC_332_246,(0,0,4):C.UVGC_333_249})

