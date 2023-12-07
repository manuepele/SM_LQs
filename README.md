# SM_LQs
Computational tools to implement a particle physics model that involves four new scalar leptoquark fields $\chi^u_1$, $\chi^u_2$, $\chi^d_1$ and $\chi^d_2$ and their interactions to the gauge bosons of the Standard Model. The details of the model are discussed in:

- Da Rold, L., Epele, M., Medina, A. et al. Enhancement of the double Higgs production via leptoquarks at the LHC. J. High Energ. Phys. 2021, 100 (2021). arXiv:2105.06309

This tools were developes by making use of:

- **Feynrules:**
  * C. Degrande, C. Duhr, B. Fuks, D. Grellscheid, O. Mattelaer and T. Reiter, UFO - The Universal FeynRules Output, Comput. Phys. Commun. 183 (2012) 1201 [1108.2040].
  * A. Alloul, N. D. Christensen, C. Degrande, C. Duhr and B. Fuks, FeynRules 2.0 - A complete toolbox for tree-level phenomenology, Comput. Phys. Commun. 185 (2014) 2250 [1310.1921].

- **FeynArts:**
  * T. Hahn, Generating Feynman diagrams and amplitudes with FeynArts 3, Comput. Phys. Commun. 140 (2001) 418 [hep-ph/0012260].

- **NLOCT:**
  * C. Degrande, Automatic evaluation of UV and R2 terms for beyond the Standard Model Lagrangians: a proof-of-principle, Comput. Phys. Commun. 197 (2015) 239 [1406.3030].

## FeynArt model
***SM_LQs--FA*** directory contains a Feynarts model, suitable for analytical calculations. 

## MadGraph5_aMC@NLO UFO model
***SM_LQs--UFO*** directory contains a MadGraph5_aMC@NLO UFO model, ready to perform numerical simulations up to one-loop order. The model parametrization is defined setting as external parameters the gauge coupling constants $\lambda_1$, $\lambda_2$ and $\lambda_3$, the masses of the physical fields $m_{\chi^u_1}$, $m_{\chi^u_2}$, $m_{\chi^d_1}$ and $m_{\chi^d_2}$,  and $\sin(\theta_u)$.  In the code, this parameters are denoted by lam1, lam2, lam3, Mu1, Mu2, Md1, Md2, and sTu, respectively. The remaining parameters are internally computed from relations:

$${M_\bar{R_2}}^2 = m_{\chi^u_2}^2 + \(m_{\chi^u_1}^2-m_{\chi^u_2}^2\) \sin(\theta_u)^2 -\frac{\lambda_1~ v^2}{2}$$ 

$${M_\bar{S_1}}^2 = m_{\chi^u_1}^2 - \(m_{\chi^u_1}^2 - m_{\chi^u_2}^2\) \sin(\theta_u)^2 - \frac{\lambda_3~ v^2}{2}$$ 

$${M_{S_1}}^2 = m_{\chi^d_1}^2 + m_{\chi^d_2}^2  - m_{\chi^u_2}^2 - (m_{\chi^u_1}^2  - m_{\chi^u_2}^2)\sin(\theta_u)^2 - \frac{\lambda_2~ v^2}{2}$$ 

$$\sin(\theta_d) = \sqrt{\frac{m_{\chi^u_2}^2 - m_{\chi^d_2}^2 + (m_{\chi^u_1}^2 - m_{\chi^u_2}^2)\sin(\theta_u)^2}{m_{\chi^d_1}^2 - m_{\chi^d_2}^2}}$$

$$\mu_1 = \frac{(m_{\chi^d_1}^2 - m_{\chi^d_2}^2) \sin(\theta_d) \sqrt{2 - 2 \sin(\theta_d)^2}}{v}$$

$$\mu_2 = \frac{(m_{\chi^u_1}^2 - m_{\chi^u_2}^2) \sin(\theta_u) \sqrt{2 - 2 \sin(\theta_u)^2}}{v}$$

with $m_{\chi^u_1} > m_{\chi^u_2}$ and $m_{\chi^d_1} > m_{\chi^d_2}$, and $v$ denoting the Higgs vacuum expectaion value.

