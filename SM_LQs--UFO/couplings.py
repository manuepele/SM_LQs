# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 11.0.0 for Linux x86 (64-bit) (July 28, 2016)
# Date: Fri 8 Jul 2022 18:44:13


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(cTd*cTu*ee**2*complex(0,1))/(3.*cw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(cw*ee)/(2.*sw) + (ee*sw)/(2.*cw)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                  order = {'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(cTd*cw*ee*complex(0,1)*sTd)/(2.*sw) - (cTd*ee*complex(0,1)*sTd*sw)/(2.*cw)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(cTd*cw*ee*complex(0,1)*sTd)/(2.*sw) + (cTd*ee*complex(0,1)*sTd*sw)/(2.*cw)',
                  order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-G',
                 order = {'QCD':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(cTd*cw*ee**2*complex(0,1)*sTd)/(3.*sw) + (cTd*ee**2*complex(0,1)*sTd*sw)/(3.*cw)',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((cTd*cw*ee*complex(0,1)*G*sTd)/sw) - (cTd*ee*complex(0,1)*G*sTd*sw)/cw',
                  order = {'QCD':1,'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(cw*ee*complex(0,1)*sTd**2)/(2.*sw) + (cTd**2*ee*complex(0,1)*sw)/(3.*cw) - (ee*complex(0,1)*sTd**2*sw)/(6.*cw)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(cw*ee*complex(0,1)*sTd**2)/(2.*sw) - (cTd**2*ee*complex(0,1)*sw)/(3.*cw) + (ee*complex(0,1)*sTd**2*sw)/(6.*cw)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(cTd**2*cw*ee*complex(0,1))/(2.*sw) + (cTd**2*ee*complex(0,1)*sw)/(6.*cw) - (ee*complex(0,1)*sTd**2*sw)/(3.*cw)',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-(cTd**2*cw*ee*complex(0,1))/(2.*sw) - (cTd**2*ee*complex(0,1)*sw)/(6.*cw) + (ee*complex(0,1)*sTd**2*sw)/(3.*cw)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(cw*ee**2*complex(0,1)*sTd**2)/(3.*sw) - (2*cTd**2*ee**2*complex(0,1)*sw)/(9.*cw) + (ee**2*complex(0,1)*sTd**2*sw)/(9.*cw)',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '(cTd**2*cw*ee**2*complex(0,1))/(3.*sw) + (cTd**2*ee**2*complex(0,1)*sw)/(9.*cw) - (2*ee**2*complex(0,1)*sTd**2*sw)/(9.*cw)',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((cw*ee*complex(0,1)*G*sTd**2)/sw) + (2*cTd**2*ee*complex(0,1)*G*sw)/(3.*cw) - (ee*complex(0,1)*G*sTd**2*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((cTd**2*cw*ee*complex(0,1)*G)/sw) - (cTd**2*ee*complex(0,1)*G*sw)/(3.*cw) + (2*ee*complex(0,1)*G*sTd**2*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(cTu*cw*ee*complex(0,1)*sTu)/(2.*sw) - (cTu*ee*complex(0,1)*sTu*sw)/(2.*cw)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(cTu*cw*ee*complex(0,1)*sTu)/(2.*sw) + (cTu*ee*complex(0,1)*sTu*sw)/(2.*cw)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(2*cTu*cw*ee**2*complex(0,1)*sTu)/(3.*sw) + (2*cTu*ee**2*complex(0,1)*sTu*sw)/(3.*cw)',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '(cTu*cw*ee*complex(0,1)*G*sTu)/sw + (cTu*ee*complex(0,1)*G*sTu*sw)/cw',
                  order = {'QCD':1,'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '(cw*ee*complex(0,1)*sTu**2)/(2.*sw) - (2*cTu**2*ee*complex(0,1)*sw)/(3.*cw) - (ee*complex(0,1)*sTu**2*sw)/(6.*cw)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(cw*ee*complex(0,1)*sTu**2)/(2.*sw) + (2*cTu**2*ee*complex(0,1)*sw)/(3.*cw) + (ee*complex(0,1)*sTu**2*sw)/(6.*cw)',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(cTu**2*cw*ee*complex(0,1))/(2.*sw) - (cTu**2*ee*complex(0,1)*sw)/(6.*cw) - (2*ee*complex(0,1)*sTu**2*sw)/(3.*cw)',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(cTu**2*cw*ee*complex(0,1))/(2.*sw) + (cTu**2*ee*complex(0,1)*sw)/(6.*cw) + (2*ee*complex(0,1)*sTu**2*sw)/(3.*cw)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(2*cw*ee**2*complex(0,1)*sTu**2)/(3.*sw) - (8*cTu**2*ee**2*complex(0,1)*sw)/(9.*cw) - (2*ee**2*complex(0,1)*sTu**2*sw)/(9.*cw)',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '(2*cTu**2*cw*ee**2*complex(0,1))/(3.*sw) - (2*cTu**2*ee**2*complex(0,1)*sw)/(9.*cw) - (8*ee**2*complex(0,1)*sTu**2*sw)/(9.*cw)',
                  order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = 'G',
                 order = {'QCD':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(cw*ee*complex(0,1)*G*sTu**2)/sw - (4*cTu**2*ee*complex(0,1)*G*sw)/(3.*cw) - (ee*complex(0,1)*G*sTu**2*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(cTu**2*cw*ee*complex(0,1)*G)/sw - (cTu**2*ee*complex(0,1)*G*sw)/(3.*cw) - (4*ee*complex(0,1)*G*sTu**2*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '(cTd*ee**2*complex(0,1)*sTd)/3. + (cTd*cw**2*ee**2*complex(0,1)*sTd)/(2.*sw**2) - (cTd*ee**2*complex(0,1)*sTd*sw**2)/(6.*cw**2)',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee**2*complex(0,1)*sTd**2)/3. + (cw**2*ee**2*complex(0,1)*sTd**2)/(2.*sw**2) + (2*cTd**2*ee**2*complex(0,1)*sw**2)/(9.*cw**2) + (ee**2*complex(0,1)*sTd**2*sw**2)/(18.*cw**2)',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '(cTd**2*ee**2*complex(0,1))/3. + (cTd**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cTd**2*ee**2*complex(0,1)*sw**2)/(18.*cw**2) + (2*ee**2*complex(0,1)*sTd**2*sw**2)/(9.*cw**2)',
                  order = {'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(cTu*ee**2*complex(0,1)*sTu)/3. + (cTu*cw**2*ee**2*complex(0,1)*sTu)/(2.*sw**2) - (5*cTu*ee**2*complex(0,1)*sTu*sw**2)/(6.*cw**2)',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(ee**2*complex(0,1)*sTu**2)/3. + (cw**2*ee**2*complex(0,1)*sTu**2)/(2.*sw**2) + (8*cTu**2*ee**2*complex(0,1)*sw**2)/(9.*cw**2) + (ee**2*complex(0,1)*sTu**2*sw**2)/(18.*cw**2)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(cTu**2*ee**2*complex(0,1))/3. + (cTu**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cTu**2*ee**2*complex(0,1)*sw**2)/(18.*cw**2) + (8*ee**2*complex(0,1)*sTu**2*sw**2)/(9.*cw**2)',
                  order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*G**2)',
                 order = {'QCD':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(ee**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-2*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(cTd*complex(0,1)*lam1*sTd*vev) + cTd*complex(0,1)*lam2*sTd*vev - (cTd**2*complex(0,1)*mu1)/cmath.sqrt(2) + (complex(0,1)*mu1*sTd**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-(cTd**2*complex(0,1)*lam2*vev) - complex(0,1)*lam1*sTd**2*vev - cTd*complex(0,1)*mu1*sTd*cmath.sqrt(2)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(cTd**2*complex(0,1)*lam1*vev) - complex(0,1)*lam2*sTd**2*vev + cTd*complex(0,1)*mu1*sTd*cmath.sqrt(2)',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(cTu*complex(0,1)*lam1*sTu*vev) + cTu*complex(0,1)*lam3*sTu*vev - (cTu**2*complex(0,1)*mu2)/cmath.sqrt(2) + (complex(0,1)*mu2*sTu**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-(cTu**2*complex(0,1)*lam3*vev) - complex(0,1)*lam1*sTu**2*vev - cTu*complex(0,1)*mu2*sTu*cmath.sqrt(2)',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(cTu**2*complex(0,1)*lam1*vev) - complex(0,1)*lam3*sTu**2*vev + cTu*complex(0,1)*mu2*sTu*cmath.sqrt(2)',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = 'yb/cmath.sqrt(2)',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(CKM1x3*yb)',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-(CKM2x3*yb)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(CKM3x3*yb)',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-(yc/cmath.sqrt(2))',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = 'yc/cmath.sqrt(2)',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = 'CKM2x1*yc',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = 'CKM2x2*yc',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = 'CKM2x3*yc',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-(ydo/cmath.sqrt(2))',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = 'ydo/cmath.sqrt(2)',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-(CKM1x1*ydo)',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-(CKM2x1*ydo)',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-(CKM3x1*ydo)',
                  order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_180 = Coupling(name = 'GC_180',
                  value = '-ye',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = 'ye',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-(ye/cmath.sqrt(2))',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = 'ye/cmath.sqrt(2)',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-ym',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = 'ym',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-(ym/cmath.sqrt(2))',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = 'ym/cmath.sqrt(2)',
                  order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(cTu*ee**2*complex(0,1)*sTd)/(3.*cw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '-(ys/cmath.sqrt(2))',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = 'ys/cmath.sqrt(2)',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-(CKM1x2*ys)',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-(CKM2x2*ys)',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-(CKM3x2*ys)',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = 'CKM3x1*yt',
                  order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(cTd*complex(0,1)*lam1*sTd) + cTd*complex(0,1)*lam2*sTd',
                 order = {'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = 'CKM3x2*yt',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = 'CKM3x3*yt',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-ytau',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = 'ytau',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-(yup/cmath.sqrt(2))',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = 'yup/cmath.sqrt(2)',
                  order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(cTd**2*ee*complex(0,1))/3. + (ee*complex(0,1)*sTd**2)/3.',
                 order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = 'CKM1x1*yup',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = 'CKM1x2*yup',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = 'CKM1x3*yup',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(yup*complexconjugate(CKM1x1))',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = 'ys*complexconjugate(CKM1x2)',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-(yup*complexconjugate(CKM1x2))',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(2*cTd**2*ee**2*complex(0,1))/9. + (2*ee**2*complex(0,1)*sTd**2)/9.',
                 order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = 'yb*complexconjugate(CKM1x3)',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-(yup*complexconjugate(CKM1x3))',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-(yc*complexconjugate(CKM2x1))',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-(yc*complexconjugate(CKM2x2))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = 'ys*complexconjugate(CKM2x2)',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = 'yb*complexconjugate(CKM2x3)',
                  order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(cTd**2*complex(0,1)*G) - complex(0,1)*G*sTd**2',
                 order = {'QCD':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-(yc*complexconjugate(CKM2x3))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-(yt*complexconjugate(CKM3x1))',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = 'ys*complexconjugate(CKM3x2)',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '-(yt*complexconjugate(CKM3x2))',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = 'yb*complexconjugate(CKM3x3)',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '-(yt*complexconjugate(CKM3x3))',
                  order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(-2*cTd**2*ee*complex(0,1)*G)/3. - (2*ee*complex(0,1)*G*sTd**2)/3.',
                 order = {'QCD':1,'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = 'cTd**2*complex(0,1)*G**2 + complex(0,1)*G**2*sTd**2',
                 order = {'QCD':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(cTd**2*complex(0,1)*lam2) - complex(0,1)*lam1*sTd**2',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(cTd**2*complex(0,1)*lam1) - complex(0,1)*lam2*sTd**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-((cTd**2*mu1)/cmath.sqrt(2)) - (mu1*sTd**2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cTd**2*mu1)/cmath.sqrt(2) + (mu1*sTd**2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-(cTd*ee**2*complex(0,1)*sTu)/(3.*cw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(ee**2*complex(0,1)*sTd*sTu)/(3.*cw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(cTu*complex(0,1)*lam1*sTu) + cTu*complex(0,1)*lam3*sTu',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = 'cTu*mu2*sTd - cTd*mu1*sTu',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(cTu*mu2*sTd) + cTd*mu1*sTu',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = 'cTu*mu1*sTd - cTd*mu2*sTu',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-(cTu*mu1*sTd) + cTd*mu2*sTu',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(cTd*cTu*mu2) - mu1*sTd*sTu',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'cTd*cTu*mu2 + mu1*sTd*sTu',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(cTd*cTu*mu1) - mu2*sTd*sTu',
                 order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'cTd*cTu*mu1 + mu2*sTd*sTu',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(-2*cTu**2*ee*complex(0,1))/3. - (2*ee*complex(0,1)*sTu**2)/3.',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(8*cTu**2*ee**2*complex(0,1))/9. + (8*ee**2*complex(0,1)*sTu**2)/9.',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(cTu**2*complex(0,1)*G) - complex(0,1)*G*sTu**2',
                 order = {'QCD':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(4*cTu**2*ee*complex(0,1)*G)/3. + (4*ee*complex(0,1)*G*sTu**2)/3.',
                 order = {'QCD':1,'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = 'cTu**2*complex(0,1)*G**2 + complex(0,1)*G**2*sTu**2',
                 order = {'QCD':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(cTu**2*complex(0,1)*lam3) - complex(0,1)*lam1*sTu**2',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(cTu**2*complex(0,1)*lam1) - complex(0,1)*lam3*sTu**2',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((cTu**2*mu2)/cmath.sqrt(2)) - (mu2*sTu**2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cTu**2*mu2)/cmath.sqrt(2) + (mu2*sTu**2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cTd**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cTu**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(-2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(cTd*ee**2*complex(0,1)*sTd)/(2.*sw**2)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee**2*complex(0,1)*sTd**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cTu*ee**2*complex(0,1)*sTu)/(2.*sw**2)',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(ee**2*complex(0,1)*sTu**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-ee/(2.*sw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'ee/(2.*sw)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-((cTd*cTu*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(cTd*cTu*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-ee**2/(2.*sw)',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(ee**2*complex(0,1))/(2.*sw)',
                 order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cTd*cTu*ee**2*complex(0,1))/(3.*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cTd*cTu*ee*complex(0,1)*G*cmath.sqrt(2))/sw',
                 order = {'QCD':1,'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((cTu*ee*complex(0,1)*sTd)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cTu*ee*complex(0,1)*sTd)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cTu*ee**2*complex(0,1)*sTd)/(3.*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(cTu*ee*complex(0,1)*G*sTd*cmath.sqrt(2))/sw',
                 order = {'QCD':1,'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((cTd*ee*complex(0,1)*sTu)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(cTd*ee*complex(0,1)*sTu)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(cTd*ee**2*complex(0,1)*sTu)/(3.*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cTd*ee*complex(0,1)*G*sTu*cmath.sqrt(2))/sw',
                 order = {'QCD':1,'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((ee*complex(0,1)*sTd*sTu)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1)*sTd*sTu)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee**2*complex(0,1)*sTd*sTu)/(3.*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1)*G*sTd*sTu*cmath.sqrt(2))/sw',
                 order = {'QCD':1,'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

