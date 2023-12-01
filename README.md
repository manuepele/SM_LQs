# SM_LQs
Modification of the standard model with the inclusion of scalar leptoquarks: UFO and FeynArts model.

Modification of the Standard Model which includes physical scalar leptoquarks $\chi^u_1$, $\chi^u_2$, $\chi^d_1$ and $\chi^d_2$ presented in,:

Da Rold, L., Epele, M., Medina, A. et al. Enhancement of the double Higgs production via leptoquarks at the LHC. J. High Energ. Phys. 2021, 100 (2021). arXiv:2105.06309

Directories contain Feynarts and UFO models to be used under FeynCalc/FeynArts and MadGraph5_aMC@NLO.

The parametrization of the UFO model is definde setting the gauge coupling constants $\lam_1$, $\lam_2$ and $\lam_3$, the masses of the physical fields $m_{\chi^u_1}$, $m_{\chi^u_2}$, $m_{\chi^d_1}$, $m_{\chi^d_2}$,  and $\sin(\theta_u)$ as external parameters.  In the code, this paramters are denoted by lam1, lam2, lam3, Mu1, Mu2, Md1, Md2 and sTu, respectively. The remaining paramters are internally computed from the following set of equations:
