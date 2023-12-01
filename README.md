# SM_LQs
Modification of the Standard Model which includes physical scalar leptoquarks $\chi^u_1$, $\chi^u_2$, $\chi^d_1$ and $\chi^d_2$ presented in:

- Da Rold, L., Epele, M., Medina, A. et al. Enhancement of the double Higgs production via leptoquarks at the LHC. J. High Energ. Phys. 2021, 100 (2021). arXiv:2105.06309

Directories contain Feynarts and UFO models to be used under FeynCalc/FeynArts and MadGraph5_aMC@NLO.

The UFO model parametrization is definde setting as external parameters the gauge coupling constants $\lambda_1$, $\lambda_2$ and $\lambda_3$, the masses of the physical fields $m_{\chi^u_1}$, $m_{\chi^u_2}$, $m_{\chi^d_1}$ and $m_{\chi^d_2}$,  and $\sin(\theta_u)$.  In the code, this paramters are denoted by lam1, lam2, lam3, Mu1, Mu2, Md1, Md2 and sTu, respectively. The remaining paramters are internally computed from relations:

$${M_\bar{R_2}}^2 = m_{\chi^u_2}^2 + \(m_{\chi^u_1}^2-m_{\chi^u_2}^2\) \sin(\theta_u)^2 -\frac{\lambda_1~ v^2}{2}$$ 

$${M_\bar{S_1}}^2 = m_{\chi^u_1}^2 - \(m_{\chi^u_1}^2 - m_{\chi^u_2}^2\) \sin(\theta_u)^2 - \frac{\lambda_3~ v^2}{2}$$ 

$${M_{S_1}}^2 = m_{\chi^d_1}^2 + m_{\chi^d_2}^2  - m_{\chi^u_2}^2 - (m_{\chi^u_1}^2  - m_{\chi^u_2}^2)\sin(\theta_u)^2 - \frac{\lambda_2~ v^2}{2}$$ 

$$\sin(\theta_d) = \sqrt{\frac{m_{\chi^u_2}^2 - m_{\chi^d_2}^2 + (m_{\chi^u_1}^2 - m_{\chi^u_2}^2)\sin(\theta_u)^2}{m_{\chi^d_1}^2 - m_{\chi^d_2}^2}}$$

$$\mu_1 = \frac{(m_{\chi^d_1}^2 - m_{\chi^d_2}^2) \sin(\theta_d) \sqrt{2 - 2 \sin(\theta_d)^2}}{v}$$

$$\mu_2 = \frac{(m_{\chi^u_1}^2 - m_{\chi^u_2}^2) \sin(\theta_u) \sqrt{2 - 2 \sin(\theta_u)^2}}{v}$$

with $m_{\chi^u_1} > m_{\chi^u_2}$ and $m_{\chi^d_1} > m_{\chi^d_2}$, and $v$ denoting the Higgs vacuum expectaion value.

