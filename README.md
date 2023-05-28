# Interactive NLP Papers🤖+👨‍💼📚🤗⚒️🌏 

Must-read papers on [Interactive NLP](https://arxiv.org/abs/2305.13246): a new paradigm of NLP.



## Content

- [What is Interactive NLP?](#what-is-interactive-nlp)
- [Keywords Convention](#keywords-convention)
- [Paper](#paper)
  - [Surveys and Position Papers](#surveys-and-position-papers)
  - [Human-LM Interaction](#human-lm-interaction)
  - [KB-LM Interaction](#kb-lm-interaction)
  - [Model/Tool-LM Interaction](#model-tool-lm-interaction)
  - [Environment-LM Interaction](#environment-lm-interaction)
  - [Evaluation](#evaluation)
  - [Application](#application)
- [Related Projects](#related-projects)
- [Contribution](#contribution)
  - [Contributors](#contributors)
  - [Contributing to this paper list](#contributing-to-this-paper-list)



## What is Interactive NLP?

**Interactive Natural Language Processing (iNLP)** considers language models as agents capable of observing, acting, and receiving feedback in a loop with external objects such as humans, knowledge bases, tools, models, and environments, where: 

- **Observation** involves all kinds of inputs to language models. 
- **Action** involves all kinds of outputs of language models such as text generation, requesting for external objects, text editing, etc. 
- **Feedback** involves feedback messages passed from external objects to language models such as scoring from humans.

<img src="assets/overview.png" width="60%">

In iNLP, language models can interact with four kinds of objects (i.e., entities): 

- interact with **humans** for better understanding and addressing user needs, personalizing responses, aligning with human values, and improving the overall user experience;
- interact with **knowledge bases** for enriching language representations with factual knowledge, enhancing the contextual relevance of responses, and dynamically leveraging external information to generate more accurate and informed responses;
- interact with **models/tools** for effectively decomposing and addressing complex tasks, leveraging specialized expertise for specific subtasks, and fostering the simulation of social behaviors;
- interact with **environments** for learning grounded representations of language, and effectively tackling embodied tasks such as reasoning, planning, and decision-making in response to environmental observations.



## Keywords Convention

![img](https://img.shields.io/badge/-InstructGPT-blue) The abbreviation of the work.

![img](https://img.shields.io/badge/-Prompting%20Chaining-orange) The interaction method used by the work.

![img](https://img.shields.io/badge/-formal%20language-lightgrey) The interaction interface used by the work.

![img](https://img.shields.io/badge/Other-green) Other important information of the work.



## Paper

### 🔭Surveys and Position Papers

- **[Interactive Natural Language Processing](https://arxiv.org/abs/2305.13246)**, 2023.05 ![img](https://img.shields.io/badge/Interactive_Learning-green)

  *Zekun Wang, Ge Zhang, Kexin Yang, Ning Shi, Wangchunshu Zhou, Shaochun Hao, Guangzheng Xiong, Yizhi Li, Mong Yuan Sim, Xiuying Chen, Qingqing Zhu, Zhenzhu Yang, Adam Nik, Qi Liu, Chenghua Lin, Shi Wang, Ruibo Liu, Wenhu Chen, Ke Xu, Dayiheng Liu, Yike Guo, Jie Fu*.

- **[Tool Learning with Foundation Models](https://arxiv.org/abs/2304.08354)**, 2023.04 ![img](https://img.shields.io/badge/-Tool--use-green) 

  *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang, Chaojun Xiao, Chi Han, Yi Ren Fung, Yusheng Su, Huadong Wang, Cheng Qian, Runchu Tian, Kunlun Zhu, Shihao Liang, Xingyu Shen, Bokai Xu, Zhen Zhang, Yining Ye, Bowen Li, Ziwei Tang, Jing Yi, Yuzhang Zhu, Zhenning Dai, Lan Yan, Xin Cong, Yaxi Lu, Weilin Zhao, Yuxiang Huang, Junxi Yan, Xu Han, Xian Sun, Dahai Li, Jason Phang, Cheng Yang, Tongshuang Wu, Heng Ji, Zhiyuan Liu, Maosong Sun*.

- **[Augmented Language Models: a Survey](https://arxiv.org/abs/2302.07842)**, 2023.02 ![img](https://img.shields.io/badge/-Reasoning-green) ![img](https://img.shields.io/badge/-Tool--use-green)

  *Grégoire Mialon, Roberto Dessì, Maria Lomeli, Christoforos Nalmpantis, Ram Pasunuru, Roberta Raileanu, Baptiste Rozière, Timo Schick, Jane Dwivedi-Yu, Asli Celikyilmaz, Edouard Grave, Yann LeCun, Thomas Scialom*.

- **[Foundation Models for Decision Making: Problems, Methods, and Opportunities](https://arxiv.org/abs/2303.04129)**, 2023.03 ![img](https://img.shields.io/badge/-Tool--use-green) ![img](https://img.shields.io/badge/-Decision%20Making-green)

  *Sherry Yang, Ofir Nachum, Yilun Du, Jason Wei, Pieter Abbeel, Dale Schuurmans*.

### 👨‍💼Human-LM Interaction

- **[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)**, 2022.03 ![img](https://img.shields.io/badge/-InstructGPT-blue) ![img](https://img.shields.io/badge/-Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/Feedback-green)

  *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe*.

- **[Deep reinforcement learning from human preferences](https://arxiv.org/abs/1706.03741)**, 2017.06 ![img](https://img.shields.io/badge/-Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/Feedback-green)

  *Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, Dario Amodei*.

- **[Improving alignment of dialogue agents via targeted human judgements](https://arxiv.org/abs/2209.14375)**, 2022.09 ![img](https://img.shields.io/badge/-Sparrow-blue) ![img](https://img.shields.io/badge/-Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/Feedback-green)

  *Amelia Glaese, Nat McAleese, Maja Trębacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger, Martin Chadwick, Phoebe Thacker, Lucy Campbell-Gillingham, Jonathan Uesato, Po-Sen Huang, Ramona Comanescu, Fan Yang, Abigail See, Sumanth Dathathri, Rory Greig, Charlie Chen, Doug Fritz, Jaume Sanchez Elias, Richard Green, Soňa Mokrá, Nicholas Fernando, Boxi Wu, Rachel Foley, Susannah Young, Iason Gabriel, William Isaac, John Mellor, Demis Hassabis, Koray Kavukcuoglu, Lisa Anne Hendricks, Geoffrey Irving*.

- **[AI Chains](https://arxiv.org/abs/2110.01691)**, 2021.1 ![img](https://img.shields.io/badge/-AI%20Chains-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Configuration-green)

  *Tongshuang Wu, Michael Terry, Carrie J. Cai*.

- **[Interactive Text Generation](https://arxiv.org/abs/2303.00908)**, 2023.03 ![img](https://img.shields.io/badge/-ITG-blue) ![img](https://img.shields.io/badge/-Imitation%20Learning-orange) ![img](https://img.shields.io/badge/-Edits-lightgrey) ![img](https://img.shields.io/badge/Simulation-green)

  *Felix Faltings, Michel Galley, Baolin Peng, Kianté Brantley, Weixin Cai, Yizhe Zhang, Jianfeng Gao, Bill Dolan*.

- **[PromptChainer](https://arxiv.org/abs/2203.06566)**, 2022.03 ![img](https://img.shields.io/badge/-PromptChainer-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Configuration-green)

  *Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff Gray, Alejandra Molina, Michael Terry, Carrie J Cai*.

- **[RRHF: Rank Responses to Align Language Models with Human Feedback without tears](https://arxiv.org/abs/2304.05302)**, 2023.04 ![img](https://img.shields.io/badge/-RRHF-blue) ![img](https://img.shields.io/badge/-Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/Feedback-green)

  *Zheng Yuan, Hongyi Yuan, Chuanqi Tan, Wei Wang, Songfang Huang, Fei Huang*.

- **[RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment](https://arxiv.org/abs/2304.06767)**, 2023.04 ![img](https://img.shields.io/badge/-RAFT-blue) ![img](https://img.shields.io/badge/Feedback-green)

  *Hanze Dong, Wei Xiong, Deepanshu Goyal, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, Tong Zhang*.

- **[Interactive Language: Talking to Robots in Real Time](https://arxiv.org/abs/2210.06407)**, 2022.1 ![img](https://img.shields.io/badge/-Interactive%20Language-blue) ![img](https://img.shields.io/badge/-Imitation%20Learning-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Chat-green)

  *Corey Lynch, Ayzaan Wahid, Jonathan Tompson, Tianli Ding, James Betker, Robert Baruch, Travis Armstrong, Pete Florence*.

- **[Improving Grounded Language Understanding in a Collaborative Environment by Interacting with Agents Through Help Feedback](https://arxiv.org/abs/2304.10750)**, 2023.04 ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Chat,%20Feedback-green)

  *Nikhil Mehta, Milagro Teruel, Patricio Figueroa Sanz, Xin Deng, Ahmed Hassan Awadallah, Julia Kiseleva*.

- **[Is Reinforcement Learning (Not) for Natural Language Processing: Benchmarks, Baselines, and Building Blocks for Natural Language Policy Optimization](https://arxiv.org/abs/2210.01241)**, 2022.1 ![img](https://img.shields.io/badge/-RL4LMs-blue) ![img](https://img.shields.io/badge/-Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/Feedback-green)

  *Rajkumar Ramamurthy, Prithviraj Ammanabrolu, Kianté Brantley, Jack Hessel, Rafet Sifa, Christian Bauckhage, Hannaneh Hajishirzi, Yejin Choi*.

- **[Improving Multimodal Interactive Agents with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2211.11602)**, 2022.11 ![img](https://img.shields.io/badge/-IBT-blue) ![img](https://img.shields.io/badge/-Imitation%20Learning,%20Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/Feedback-green)

  *Josh Abramson, Arun Ahuja, Federico Carnevale, Petko Georgiev, Alex Goldin, Alden Hung, Jessica Landon, Jirka Lhotka, Timothy Lillicrap, Alistair Muldal, George Powell, Adam Santoro, Guy Scully, Sanjana Srivastava, Tamara von Glehn, Greg Wayne, Nathaniel Wong, Chen Yan, Rui Zhu*.

- **[Towards Teachable Reasoning Systems: Using a Dynamic Memory of User Feedback for Continual System Improvement](https://arxiv.org/abs/2204.13074)**, 2022.04 ![img](https://img.shields.io/badge/-TeachMe-blue) ![img](https://img.shields.io/badge/-Continual%20Learning-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Feedback-green)

  *Bhavana Dalvi Mishra, Oyvind Tafjord, Peter Clark*.

- **[MemPrompt: Memory-assisted Prompt Editing with User Feedback](https://aclanthology.org/2022.emnlp-main.183.pdf)**, 2022.12 ![img](https://img.shields.io/badge/-MemPrompt-blue) ![img](https://img.shields.io/badge/-Active%20Learning-orange) ![img](https://img.shields.io/badge/-Edits-lightgrey) ![img](https://img.shields.io/badge/Personalization,%20Feedback-green)

  *Aman Madaan, Niket Tandon, Peter Clark, Yiming Yang*.

- **[Constitutional Al:learning from ai feedback](https://arxiv.org/abs/2212.08073)**, 2022.12 ![img](https://img.shields.io/badge/-Constitutional%20AI-blue) ![img](https://img.shields.io/badge/-Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/Feedback-green)

  *Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, Jared Kaplan*.

- **[Craft an Iron Sword: Dynamically Generating Interactive Game Characters by Prompting Large Language Models Tuned on Code](https://aclanthology.org/2022.wordplay-1.3/)**, 2022.01 ![img](https://img.shields.io/badge/Game,%20Chat-green)

  *Volum, Ryan and Rao, Sudha and Xu, Michael and DesGarennes, Gabriel A and Brockett, Chris and Van Durme, Benjamin and Deng, Olivia and Malhotra, Akanksha and Dolan, Bill*.

- **[LaMP: When Large Language Models Meet Personalization](https://arxiv.org/abs/2304.11406)**, 2023.04 ![img](https://img.shields.io/badge/-LaMP-blue) ![img](https://img.shields.io/badge/Personalization-green)

  *Alireza Salemi, Sheshera Mysore, Michael Bendersky, Hamed Zamani*.

- **[Languages are Rewards: Hindsight Finetuning using Human Feedback](https://arxiv.org/abs/2302.02676)**, 2023.02 ![img](https://img.shields.io/badge/-Chain%20of%20Hindsight-blue) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Feedback-green)

  *Hao Liu, Carmelo Sferrazza, Pieter Abbeel*.

- **[InternChat: Solving Vision-Centric Tasks by Interacting with Chatbots Beyond Language](https://arxiv.org/abs/2305.05662)**, 2023.05 ![img](https://img.shields.io/badge/-InternChat-blue) ![img](https://img.shields.io/badge/-Instruction%20Tuning-orange) ![img](https://img.shields.io/badge/Chat-green)

  *Zhaoyang Liu, Yinan He, Wenhai Wang, Weiyun Wang, Yi Wang, Shoufa Chen, Qinglong Zhang, Yang Yang, Qingyun Li, Jiashuo Yu, Kunchang Li, Zhe Chen, Xue Yang, Xizhou Zhu, Yali Wang, Limin Wang, Ping Luo, Jifeng Dai, Yu Qiao*.

- **[Improving Code Generation by Training with Natural Language Feedback](https://arxiv.org/abs/2303.16749)**, 2023.03 ![img](https://img.shields.io/badge/-ILF-blue) ![img](https://img.shields.io/badge/-Imitation%20Learning-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Feedback-green)

  *Angelica Chen, Jérémy Scheurer, Tomasz Korbak, Jon Ander Campos, Jun Shern Chan, Samuel R. Bowman, Kyunghyun Cho, Ethan Perez*.


### 📚KB-LM Interaction

### 🤖Model/🛠Tool-LM Interaction

### 🌎Environment-LM Interaction

### 👍Evaluation

### 🎨Application



## Related Projects

- **[ToolLearningPapers](https://github.com/thunlp/)**
- **[BMTools](https://github.com/OpenBMB/BMTools)**
- **[AgentVerse](https://github.com/OpenBMB/AgentVerse)**
- **[ChatArena](https://github.com/chatarena/chatarena)**
- **[ChatGPT Plugins](https://platform.openai.com/docs/plugins/)**
- **[LangChain](https://github.com/hwchase17/langchain)**
- **[AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT)**
- **[BabyAGI](https://github.com/yoheinakajima/babyagi)**



## Contribution

### Contributors

[   ![img](https://contrib.rocks/image?repo=InteractiveNLP-Team/awesome-InteractiveNLP-papers) ](https://github.com/InteractiveNLP-Team/awesome-InteractiveNLP-papers/graphs/contributors)

### Contributing to this paper list

- There are cases where we miss important works in this field, please contribute to this repo! Thanks for the efforts in advance.
