# Analysis of Public High Schools Admitting Students by Examination in Turkey


This repo contains a flexible, easy to understand and modifiable foundation for scraping, cleaning, analyzing and visualizing **publicly available education data of Turkey.**

Code was written in Python 3.8.5

Along with the foundation, different studies can be done about high schools and universities in Turkey. We conducted a study on the efficiency of public high schools in Turkey, as detailed in the following papers:


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

## Contact Us

If you're interested in extending this work, having an idea or having any questions:
- email us @ barslan16@ku.edu.tr or asen16@ku.edu.tr

or submit an issue.

## Installation Instructions

To get started, you'll need to have Python 3.8+ installed.


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


Installation of Web Driver: You'll need to install the Web Driver to scrape data. You can follow the necessary installation steps from Selenium's documentation.

Selenium:
- See [Web Driver Installation](https://www.selenium.dev/selenium/docs/api/py/index.html#installing)


## Getting Started

### Paths
You can follow the instructions in these files to work on the analysis or data scraping part. Google colab version of the codes will be uploaded in next days.

- [`analysis`](https://github.com/asen16/high-schools-analysis/tree/main/analysis) : Shows how master data is filtered, analyzed and data visualized.
- [`data_scraping`](https://github.com/asen16/high-schools-analysis/tree/main/data_scraping): Explains how raw data is scraped from its source.

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
- We appreciate all your contributions. If you plan to contribute new Method, Data, or anything else, please see our [contribution guidelines](https://www.github.com/asen16/high-schools-analysis/blob/main/CONTRIBUTING.md).

## Changelog

For the complete release history, see [CHANGELOG.md](https://www.github.com/asen16/high-schools-analysis/blob/main/CHANGELOG.md).

## License
Analysis of Public High Schools Admitting Students by Examination in Turkey is released under the [MIT License](https://www.github.com/asen16/high-schools-analysis/blob/main/LICENSE).
