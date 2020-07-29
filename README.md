About qulacs-conda
==================

Home: https://github.com/qulacs/qulacs

Package license: MIT

Feedstock license: BSD-3-Clause

Summary: Qulacs is a Variational Quantum Circuit Simulator for Quantum Computation Research.



Current build status
====================


<table>
    
  <tr>
    <td>Azure</td>
    <td>
      <details>
        <summary>
          <a href="https://dev.azure.com/nsls2forge/nsls2forge/_build/latest?definitionId=235&branchName=master">
            <img src="https://dev.azure.com/nsls2forge/nsls2forge/_apis/build/status/qulacs-feedstock?branchName=master">
          </a>
        </summary>
        <table>
          <thead><tr><th>Variant</th><th>Status</th></tr></thead>
          <tbody><tr>
              <td>linux_64</td>
              <td>
                <a href="https://dev.azure.com/nsls2forge/nsls2forge/_build/latest?definitionId=235&branchName=master">
                  <img src="https://dev.azure.com/nsls2forge/nsls2forge/_apis/build/status/qulacs-feedstock?branchName=master&jobName=linux&configuration=linux_64_" alt="variant">
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </details>
    </td>
  </tr>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-qulacs--conda-green.svg)](https://anaconda.org/nsls2forge/qulacs-conda) | [![Conda Downloads](https://img.shields.io/conda/dn/nsls2forge/qulacs-conda.svg)](https://anaconda.org/nsls2forge/qulacs-conda) | [![Conda Version](https://img.shields.io/conda/vn/nsls2forge/qulacs-conda.svg)](https://anaconda.org/nsls2forge/qulacs-conda) | [![Conda Platforms](https://img.shields.io/conda/pn/nsls2forge/qulacs-conda.svg)](https://anaconda.org/nsls2forge/qulacs-conda) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-qulacs--gpu-green.svg)](https://anaconda.org/nsls2forge/qulacs-gpu) | [![Conda Downloads](https://img.shields.io/conda/dn/nsls2forge/qulacs-gpu.svg)](https://anaconda.org/nsls2forge/qulacs-gpu) | [![Conda Version](https://img.shields.io/conda/vn/nsls2forge/qulacs-gpu.svg)](https://anaconda.org/nsls2forge/qulacs-gpu) | [![Conda Platforms](https://img.shields.io/conda/pn/nsls2forge/qulacs-gpu.svg)](https://anaconda.org/nsls2forge/qulacs-gpu) |

Installing qulacs-conda
=======================

Installing `qulacs-conda` from the `nsls2forge` channel can be achieved by adding `nsls2forge` to your channels with:

```
conda config --add channels nsls2forge
```

Once the `nsls2forge` channel has been enabled, `qulacs-conda, qulacs-gpu` can be installed with:

```
conda install qulacs-conda qulacs-gpu
```

It is possible to list all of the versions of `qulacs-conda` available on your platform with:

```
conda search qulacs-conda --channel nsls2forge
```




Updating qulacs-conda-feedstock
===============================

If you would like to improve the qulacs-conda recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`nsls2forge` channel, whereupon the built conda packages will be available for
everybody to install and use from the `nsls2forge` channel.
Note that all branches in the nsls-ii-forge/qulacs-conda-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================

* [@leofang](https://github.com/leofang/)

