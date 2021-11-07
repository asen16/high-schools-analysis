# Analysis of Public High Schools Admitting Students by Examination in Turkey

This repo contains an implementation of Foundation, a framework for flexible, modular, and composable environments that **model socio-economic behaviors and dynamics in a society with both agents and governments**.

Code was written in Python 3.6


This simulation can be used in conjunction with reinforcement learning to learn optimal economic policies, as detailed in the following papers:

**[Analysis of Public High Schools Admitting Students by Examination in Turkey](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3939070)**,
*Beyza Arslan, Anıl Şen.*


If you use this code or data in your research, please cite us using this BibTeX entry:

```
@article{arslan2021analysis,
  title={Analysis of Public High Schools Admitting Students by Examination in Turkey},
  author={Arslan, Beyza and {\c{S}}en, An{\i}l},
  journal={Available at SSRN 3939070},
  year={2021}
}
```



## Simulation Cards: Ethics Review and Intended Use

Please see our [Simulation Card](https://github.com/salesforce/ai-economist/blob/master/Simulation_Card_Foundation_Economic_Simulation_Framework.pdf) for a review of the intended use and ethical review of our framework.

Please see our [COVID-19 Simulation Card](https://github.com/salesforce/ai-economist/blob/master/COVID-19_Simulation-Card.pdf) for a review of the ethical aspects of the pandemic simulation (and as fitted for COVID-19).

## Contact Us

If you're interested in extending this work, having an idea or having any questions:
- email us @ barslan16@ku.edu.tr or asen16@ku.edu.tr.

## Installation Instructions

To get started, you'll need to have Python 3.6+ installed.


### Installing from Source

1. Clone this repository to your local machine:

  ```
   git clone www.github.com/asen16/high-schools-analysis
   ```

2. Change directory to the directory where requirements.txt is located.


  ```pyfunctiontypecomment
   cd [Path]
   ```

3. Run:

 ```pyfunctiontypecomment
   pip install -r requirements.txt
   ```
   in your shell.

   OR

   b) Install as an editable Python package
  ```pyfunctiontypecomment
   cd ai-economist
   pip install -e .
   ```

Useful tip: for quick access, add the following to your ~/.bashrc or ~/.bash_profile:

```pyfunctiontypecomment
alias aiecon="conda activate ai-economist; cd <local path to ai-economist>"
```

You can then simply run `aiecon` once to activate the conda environment.

### Testing your Install

To test your installation, try running:

```
conda activate ai-economist
python -c "import ai_economist"
```

## Getting Started

### Tutorials

To familiarize yourself with Foundation, check out the tutorials in the `tutorials` folder. You can run these notebooks interactively in your browser on Google Colab.

- [tutorials/economic_simulation_basic.ipynb](https://www.github.com/salesforce/ai-economist/blob/master/tutorials/economic_simulation_basic.ipynb) ([Try this on Colab](http://colab.research.google.com/github/salesforce/ai-economist/blob/master/tutorials/economic_simulation_basic.ipynb)!): Shows how to interact with and visualize the simulation.
- [tutorials/economic_simulation_advanced.ipynb](https://www.github.com/salesforce/ai-economist/blob/master/tutorials/economic_simulation_advanced.ipynb) ([Try this on Colab](http://colab.research.google.com/github/salesforce/ai-economist/blob/master/tutorials/economic_simulation_advanced.ipynb)!): Explains how Foundation is built up using composable and flexible building blocks.
- [tutorials/covid19_and_economic_simulation.ipynb](https://www.github.com/salesforce/ai-economist/blob/master/tutorials/covid19_and_economic_simulation.ipynb) ([Try this on Colab](http://colab.research.google.com/github/salesforce/ai-economist/blob/master/tutorials/covid19_and_economic_simulation.ipynb)!): A tutorial on how to work specifically with the COVID-19 pandemic and economy simulation.

To run these notebooks *locally*, you need [Jupyter](https://jupyter.org). See [https://jupyter.readthedocs.io/en/latest/install.html](https://jupyter.readthedocs.io/en/latest/install.html) for installation instructions and [(https://jupyter-notebook.readthedocs.io/en/stable/](https://jupyter-notebook.readthedocs.io/en/stable/) for examples of how to work with Jupyter.

## Structure of the Code

- The simulation is located in the `ai_economist/foundation` folder.

The code repository is organized into the following components:

| Component | Description |
| --- | --- |
| [base](https://www.github.com/salesforce/ai-economist/blob/master/ai_economist/foundation/base) | Contains base classes to can be extended to define Agents, Components and Scenarios. |
| [agents](https://www.github.com/salesforce/ai-economist/blob/master/ai_economist/foundation/agents) | Agents represent economic actors in the environment. Currently, we have mobile Agents (representing workers) and a social planner (representing a government). |
| [entities](https://www.github.com/salesforce/ai-economist/blob/master/ai_economist/foundation/entities) | Endogenous and exogenous components of the environment. Endogenous entities include labor, while exogenous entity includes landmarks (such as Water and Grass) and collectible Resources (such as Wood and Stone). |
| [components](https://www.github.com/salesforce/ai-economist/blob/master/ai_economist/foundation/components) | Components are used to add some particular dynamics to an environment. They also add action spaces that define how Agents can interact with the environment via the Component. |
| [scenarios](https://www.github.com/salesforce/ai-economist/blob/master/ai_economist/foundation/scenarios) | Scenarios compose Components to define the dynamics of the world. It also computes rewards and exposes states for visualization. |

- The datasets (including the real-world data on COVID-19) are located in the `ai_economist/datasets` folder.

## Releases and Contributing

- Please let us know if you encounter any bugs by filing a Github issue.
- We appreciate all your contributions. If you plan to contribute new Components, Scenarios Entities, or anything else, please see our [contribution guidelines](https://www.github.com/asen16/high-schools-analysis/blob/main/CONTRIBUTING.md).

## Changelog

For the complete release history, see [CHANGELOG.md](https://www.github.com/asen16/high-schools-analysis/blob/main/CHANGELOG.md).

## License
Analysis of Public High Schools Admitting Students by Examination in Turkey is released under the [MIT License](https://www.github.com/asen16/high-schools-analysis/blob/main/LICENSE).
