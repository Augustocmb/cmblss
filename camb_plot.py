{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d152a1d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using CAMB 1.3.5 installed at /home/akozameh/miniconda3/envs/CMB/lib/python3.10/site-packages/camb\n",
      "total\n",
      "unlensed_scalar\n",
      "unlensed_total\n",
      "lensed_scalar\n",
      "tensor\n",
      "lens_potential\n",
      "(3051, 4)\n"
     ]
    }
   ],
   "source": [
    "# camb_plot.py\n",
    "\n",
    "import sys\n",
    "import platform\n",
    "import os\n",
    "import matplotlib\n",
    "from matplotlib import pyplot as plt\n",
    "import numpy as np\n",
    "import camb\n",
    "from camb import model, initialpower\n",
    "\n",
    "def plot_camb():\n",
    "    %matplotlib inline\n",
    "    %config InlineBackend.figure_format = 'retina'\n",
    "\n",
    "    print('Using CAMB %s installed at %s' % (camb.__version__, os.path.dirname(camb.__file__)))\n",
    "\n",
    "    # Add the rest of your code here\n",
    "    # ...\n",
    "    #Set up a new set of parameters for CAMB\n",
    "    #The defaults give one massive neutrino and helium set using BBN consistency\n",
    "    pars = camb.set_params(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06,  \n",
    "                       As=2e-9, ns=0.965, halofit_version='mead', lmax=3000)\n",
    "    #calculate results for these parameters\n",
    "    results = camb.get_results(pars)\n",
    "    #get dictionary of CAMB power spectra\n",
    "    powers =results.get_cmb_power_spectra(pars, CMB_unit='muK')\n",
    "    for name in powers: print(name)\n",
    "    #plot the total lensed CMB power spectra versus unlensed, and fractional difference\n",
    "    totCL=powers['total']\n",
    "    unlensedCL=powers['unlensed_scalar']\n",
    "    print(totCL.shape)\n",
    "    #Python CL arrays are all zero based (starting at L=0), Note L=0,1 entries will be zero by default.\n",
    "    #The different CL are always in the order TT, EE, BB, TE (with BB=0 for unlensed scalar results).\n",
    "    ls = np.arange(totCL.shape[0])\n",
    "\n",
    "# If you want to execute the code, call the plot_camb function\n",
    "if __name__ == \"__main__\":\n",
    "    plot_camb()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9642b9d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
