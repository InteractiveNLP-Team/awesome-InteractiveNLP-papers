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

- **[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)**, 2023.04 ![img](https://img.shields.io/badge/-Generative%20Agents-blue) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Society-green)

  *Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein*.

- **[ReAct: Synergizing reasoning and acting in language models](https://arxiv.org/abs/2210.03629)**, 2022.01 ![img](https://img.shields.io/badge/-ReAct-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Chain%20of%20Thought,%20Tool-use-green)

  *Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao*.

- **[Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models](https://arxiv.org/abs/2303.04671)**, 2023.05 ![img](https://img.shields.io/badge/-Visual%20ChatGPT-blue) ![img](https://img.shields.io/badge/Chain%20of%20Thought,%20Tool-use-green)

  *Chenfei Wu, Shengming Yin, Weizhen Qi, Xiaodong Wang, Zecheng Tang, Nan Duan*.

- **[HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580)**, 2023.05 ![img](https://img.shields.io/badge/-HuggingGPT-blue) ![img](https://img.shields.io/badge/Tool-use-green)

  *Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, Yueting Zhuang*.

- **[CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](https://arxiv.org/abs/2303.17760)**, 2023.03 ![img](https://img.shields.io/badge/-CAMEL-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Society-green)

  *Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem*.

- **[Socratic Models: Composing Zero-Shot Multimodal Reasoning with Language](https://arxiv.org/abs/2204.00598)**, 2022.05 ![img](https://img.shields.io/badge/-Socratic%20Model-blue) ![img](https://img.shields.io/badge/Communication-green)

  *Andy Zeng, Maria Attarian, Brian Ichter, Krzysztof Choromanski, Adrian Wong, Stefan Welker, Federico Tombari, Aveek Purohit, Michael Ryoo, Vikas Sindhwani, Johnny Lee, Vincent Vanhoucke, Pete Florence*.

- **[MindCraft: Theory of Mind Modeling for Situated Dialogue in Collaborative Tasks](https://arxiv.org/abs/2109.06275)**, 2021.09 ![img](https://img.shields.io/badge/-MindCraft-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Theory%20of%20Mind,%20Communication-green)

  *Cristian-Paul Bara, Sky CH-Wang, Joyce Chai*.

- **[Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks](https://arxiv.org/abs/2211.12588)**, 2022.11 ![img](https://img.shields.io/badge/-PoT%20Prompting-blue) ![img](https://img.shields.io/badge/-Elicitive%20Prompting-orange) ![img](https://img.shields.io/badge/-Formal%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use,%20Chain%20of%20Thought-green)

  *Wenhu Chen, Xueguang Ma, Xinyi Wang, William W. Cohen*.

- **[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)**, 2023.02 ![img](https://img.shields.io/badge/-Toolformer-blue) ![img](https://img.shields.io/badge/Tool-use-green)

  *Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom*.

- **[ART: Automatic multi-step reasoning and tool-use for large language models](https://arxiv.org/abs/2303.09014)**, 2023.03 ![img](https://img.shields.io/badge/-ART-blue) ![img](https://img.shields.io/badge/-Formal%20Language,%20Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use,%20Chain%20of%20Thought-green)

  *Bhargavi Paranjape, Scott Lundberg, Sameer Singh, Hannaneh Hajishirzi, Luke Zettlemoyer, Marco Tulio Ribeiro*.

- **[Small Models are valuable Plug-ins for large language models](https://arxiv.org/pdf/2305.08848.pdf)**, 2023.05 ![img](https://img.shields.io/badge/-SuperICL-blue) ![img](https://img.shields.io/badge/-Standard%20Prompting-orange)

  *Canwen Xu, Yichong Xu, Shuohang Wang, Yang Liu, Chenguang Zhu, Julian McAuley*.

- **[LEAST-TO-MOST PROMPTINGENABLESCOMPLEXREASONING IN LARGE LANGUAGE MODELS](https://arxiv.org/abs/2205.10625)**, 2022.05 ![img](https://img.shields.io/badge/-least-to-most%20prompting-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, Ed Chi*.

- **[Decomposed Prompting: A Modular Approach for Solving Complex Tasks](https://arxiv.org/abs/2210.02406)**, 2022.01 ![img](https://img.shields.io/badge/-Decomposed%20Prompting-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Tushar Khot, Harsh Trivedi, Matthew Finlayson, Yao Fu, Kyle Richardson, Peter Clark, Ashish Sabharwal*.

- **[ViperGPT: Visual Inference via Python Execution for Reasoning](https://arxiv.org/pdf/2303.08128.pdf)**, 2023.03 ![img](https://img.shields.io/badge/-ViperGPT-blue) ![img](https://img.shields.io/badge/-Elicitive%20Prompting-orange) ![img](https://img.shields.io/badge/-Formal%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Dídac Surís,  Sachit Menon, Carl Vondrick*.

- **[See,Think,Confirm:Interactive Prompting Between Vision and Language Models for Knowledge-based Visual Reasoning](https://arxiv.org/pdf/2301.05226.pdf)**, 2023.01 ![img](https://img.shields.io/badge/-IPVR-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Tool-use-green)

  *Zhenfang Chen, Qinhong Zhou, Yikang Shen, Yining Hong, Hao Zhang, Chuang Gan*.

- **[Large Language Models Are Reasoning Teachers](https://arxiv.org/abs/2212.10071)**, 2022.12 ![img](https://img.shields.io/badge/-Fine-tune-CoT-blue) ![img](https://img.shields.io/badge/-Semi-Supervised%20Fine-Tuning,%20Elicitive%20Prompting-orange) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Namgyu Ho, Laura Schmid, Se-Young Yun*.

- **[STaR:Self-Taught ReasonerBootstrapping Reasoning With Reasoning](https://arxiv.org/pdf/2203.14465.pdf)**, 2022.03 ![img](https://img.shields.io/badge/-STaR-blue) ![img](https://img.shields.io/badge/-Elicitive%20Prompting,%20Semi-Supervised%20Fine-Tuning-orange) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman*.

- **[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/pdf/2305.10601.pdf)**, 2023.05 ![img](https://img.shields.io/badge/-ToT-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan*.

- **[Search-in-the-Chain: Towards Accurate, Credible and Traceable Large Language Models for Knowledge-intensive Tasks](https://arxiv.org/pdf/2304.14732v4.pdf)**, 2023.04 ![img](https://img.shields.io/badge/-SearChain-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Tool-use,%20Chain%20of%20Thought-green)

  *Shicheng Xu, Liang Pang, HuaWei Shen, Xueqi Cheng, Tat-Seng Chua*.

- **[RECURRENTGPT: Interactive Generation of (Arbitrarily) Long Text](https://arxiv.org/pdf/2305.13304v1.pdf)**, 2023.05 ![img](https://img.shields.io/badge/-RecurrentGPT-blue) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey)

  *Wangchunshu Zhou, Yuchen Eleanor Jiang, Peng Cui, Tiannan Wang, Zhenxin Xiao, Yifan Hou, Ryan Cotterell, Mrinmaya Sachan*.

- **[PAL: Program-aided Language Models](https://arxiv.org/pdf/2211.10435v2.pdf)**, 2022.11 ![img](https://img.shields.io/badge/-PAL-blue) ![img](https://img.shields.io/badge/-Elicitive%20Prompting-orange) ![img](https://img.shields.io/badge/-Formal%20Language-lightgrey) ![img](https://img.shields.io/badge/Chain%20of%20Thought,%20Tool-use-green)

  *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, PengFei Liu, Yiming Yang, Jamie Callan, Graham Neubig*.

- **[Internet-augmented language models through few-shot prompting for open-domain question answering](https://arxiv.org/pdf/2203.05115v2.pdf)**, 2023.05 ![img](https://img.shields.io/badge/Tool-use-green)

  *Angeliki Lazaridou, Elena Gribovskaya, Wojciech Stokowiec, Nikolai Grigorev*.

- **[Recitation-Augmented Language Models](https://arxiv.org/pdf/2210.01296v2.pdf)**, 2022.01 ![img](https://img.shields.io/badge/-RECITE-blue) ![img](https://img.shields.io/badge/-Elicitive%20Prompting-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Zhiqing Sun, Xuezhi Wang, Yi Tay, Yiming Yang, Denny Zhou*.

- **[Iteratively Prompt Pre-trained Language Models for Chain of Thought](https://arxiv.org/pdf/2203.08383v3.pdf)**, 2022.03 ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Boshi Wang, Xiang Deng, Huan Sun*.

- **[MEASURING AND NARROWING THE COMPOSITIONALITY GAP IN LANGUAGE MODELS](https://arxiv.org/pdf/2210.03350v2.pdf)**, 2022.01 ![img](https://img.shields.io/badge/-self-ask-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Tool-use,%20Chain%20of%20Thought-green)

  *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith, Mike Lewis*.

- **[Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/pdf/2303.17651v1.pdf)**, 2023.03 ![img](https://img.shields.io/badge/-self-refine-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Self-Interaction-green)

  *Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Sean Welleck, Bodhisattwa Prasad Majumder, Shashank Gupta, Amir Yazdanbakhsh, Peter Clark*.

- **[LEVER: Learning to Verify Language-to-Code Generation with Execution](https://arxiv.org/pdf/2302.08468v1.pdf)**, 2023.02 ![img](https://img.shields.io/badge/-LEVER-blue) ![img](https://img.shields.io/badge/-Standard%20Prompting-orange) ![img](https://img.shields.io/badge/-Formal%20Language,%20Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Ansong Ni, Srini Iyer, Dragomir Radev, Ves Stoyanov, Wen-tau Yih, Sida I. Wang, Xi Victoria Lin*.

- **[Computational Language Acquisition with Theory of Mind](https://arxiv.org/pdf/2303.01502v1.pdf)**, 2023.03 ![img](https://img.shields.io/badge/Theory%20of%20Mind-green)

  *Andy Liu, Hao Zhu, Emmy Liu, Yonatan Bisk, Graham Neubig*.

- **[Few-shot Language Coordination by Modeling Theory of Mind](https://arxiv.org/pdf/2107.05697v1.pdf)**, 2021.07 ![img](https://img.shields.io/badge/Theory%20of%20Mind-green)

  *Hao Zhu, Graham Neubig, Yonatan Bisk*.

- **[OpenAGI: When LLM Meets Domain Experts](https://arxiv.org/pdf/2304.04370v2.pdf)**, 2023.04 ![img](https://img.shields.io/badge/-OpenAGI-blue) ![img](https://img.shields.io/badge/-Standard%20Prompting,%20Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Yingqiang Ge, Wenyue Hua, Jianchao Ji, Juntao Tan, Shuyuan Xu, Yongfeng Zhang*.

- **[MM-ReAct](https://arxiv.org/pdf/2303.11381v1.pdf)**, 2023.03 ![img](https://img.shields.io/badge/-MM-ReAct-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Tool-use-green)

  *Zhengyuan Yang, Linjie Li, JianFeng Wang, Kevin Lin, Ehsan Azarnasab, Faisal Ahmed, Zicheng Liu, Ce Liu, Michael Zeng, Lijuan Wang*.

- **[Prompt, Generate, then Cache: Cascade of Foundation Models makes Strong Few-shot Learners](https://arxiv.org/pdf/2303.02151v1.pdf)**, 2023.03 ![img](https://img.shields.io/badge/-CaFo-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language,%20Machine%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Renrui Zhang, Xiangfei Hu, Bohao Li, Siyuan Huang, Hanqiu Deng, Hongsheng Li, Yu Qiao, Peng Gao*.

- **[Principle-Driven Self-Alignment of Language Models from Scratch with Minimal Human Supervision](https://arxiv.org/pdf/2305.03047v1.pdf)**, 2023.05 ![img](https://img.shields.io/badge/-SELF-ALIGN-blue) ![img](https://img.shields.io/badge/-Instruction%20Tuning,Semi-Supervised%20Fine-Tuning-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Alignment-green)

  *Zhiqing Sun, Yikang Shen, Qinhong Zhou, Hongxin Zhang, Zhenfang Chen, David Cox, Yiming Yang, Chuang Gan*.

- **[Think Before You Act: Unified Policy for Interleaving Language Reasoning with Actions](https://arxiv.org/pdf/2304.11063v1.pdf)**, 2023.04 ![img](https://img.shields.io/badge/-Elicitive%20Prompting-orange) ![img](https://img.shields.io/badge/-Natural%20Language,%20Machine%20Language-lightgrey) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Lina Mezghani, Piotr Bojanowski, Karteek Alahari, Sainbayar Sukhbaatar*.

- **[TALM: Tool Augmented Language Models](https://arxiv.org/pdf/2205.12255v1.pdf)**, 2022.05 ![img](https://img.shields.io/badge/-TALM-blue) ![img](https://img.shields.io/badge/-Instruction%20Tuning,Semi-Supervised%20Fine-Tuning-orange) ![img](https://img.shields.io/badge/-Formal%20Language,%20Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Aaron Parisi, Yao Zhao, Noah Fiedel*.

- **[Successive Prompting for Decomposing Complex Questions](https://arxiv.org/pdf/2212.04092v1.pdf)**, 2022.12 ![img](https://img.shields.io/badge/-Successive%20Prompting-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Dheeru Dua, Shivanshu Gupta, Sameer Singh, Matt Gardner*.

- **[REFINER: Reasoning Feedback on Intermediate Representations](https://arxiv.org/pdf/2304.01904v1.pdf)**, 2023.04 ![img](https://img.shields.io/badge/-REFINER-blue) ![img](https://img.shields.io/badge/-Semi-Supervised%20Fine-Tuning,%20Elicitive%20Prompting-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Chain%20of%20Thought,%20Reasoning-green)

  *Debjit Paul, Mete Ismayilzada, Maxime Peyrard, Beatriz Borges, Antoine Bosselut, Robert West, Boi Faltings*.

- **[LeTI: Learning to Generate from Textual Interactions](https://arxiv.org/pdf/2305.10314v1.pdf)**, 2023.05 ![img](https://img.shields.io/badge/-LeTI-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Formal%20Language,%20Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Xingyao Wang, Hao Peng, Reyhaneh Jabbarvand, Heng Ji*.

- **[InternGPT: Solving Vision-Centric Tasks by Interacting with Chatbots Beyond Language](https://arxiv.org/pdf/2305.05662v3.pdf)**, 2023.05 ![img](https://img.shields.io/badge/-InternGPT-blue) ![img](https://img.shields.io/badge/-Formal%20Language,%20Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Zhaoyang Liu, Yinan He, Wenhai Wang, Weiyun Wang, Yi Wang, Shoufa Chen, Qinglong Zhang, Yang Yang, Qingyun Li, Jiashuo Yu, Kunchang Li, Zhe Chen, Xue Yang, Xizhou Zhu, Yali Wang, LiMin Wang, Ping Luo, Jifeng Dai, Yu Qiao*.

- **[Human-level play in the game of Diplomacy by combining language models with strategic reasoning](https://www.science.org/doi/10.1126/science.ade9097)**, 2022.11 ![img](https://img.shields.io/badge/-Cicero-blue) ![img](https://img.shields.io/badge/-Reinforcement%20Learning-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Decision%20Making-green)

  *Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff, Jonathan Gray, Hengyan Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath, Minae Kwon, Adam Lerer, Mike Lewis, Alexander H. Miller, Sash Mitts, Aditya Renduchintala, Stephen Roller, Dirk Rowe, Weiyan Shi, Joe Spisak, Alexander Wei, David Wu, Hugh Zhang, Markus Zijlstra*.

- **[Generating Sequences by Learning to Self-Correct](https://arxiv.org/abs/2211.00053)**, 2022.01 ![img](https://img.shields.io/badge/-Self-Correction-blue) ![img](https://img.shields.io/badge/-Semi-Supervised%20Fine-Tuning-orange) ![img](https://img.shields.io/badge/-Natural%20Language,%20Edits-lightgrey) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi, Yejin Choi*.

- **[ChatGPT-steered Editing Instructor for Customization of Abstractive Summarization](https://arxiv.org/pdf/2305.02483v1.pdf)**, 2023.05 ![img](https://img.shields.io/badge/-Semi-Supervised%20Fine-Tuning,%20Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language,%20Edits-lightgrey) ![img](https://img.shields.io/badge/Chain%20of%20Thought-green)

  *Wen Xiao, Yujia Xie, Giuseppe Carenini, Pengcheng He*.

- **[ChatGPT Asks, BLIP-2 Answers: Automatic Questioning Towards Enriched Visual Descriptions](https://arxiv.org/pdf/2303.06594v1.pdf)**, 2023.03 ![img](https://img.shields.io/badge/-ChatCaptioner-blue) ![img](https://img.shields.io/badge/-Prompt%20Chaining-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Deyao Zhu, Jun Chen, Kilichbek Haydarov, Xiaoqian Shen, Wenxuan Zhang, Mohamed Elhoseiny*.

- **[Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/pdf/2304.09842v2.pdf)**, 2023.04 ![img](https://img.shields.io/badge/-Chameleon-blue) ![img](https://img.shields.io/badge/-Formal%20Language,%20Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Tool-use-green)

  *Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu, Jianfeng Gao*.

- **[Baize: An Open-Source Chat Model with Parameter-Efficient Tuning on Self-Chat Data](https://arxiv.org/pdf/2304.01196v3.pdf)**, 2023.04 ![img](https://img.shields.io/badge/-Baize-blue) ![img](https://img.shields.io/badge/-Parameter-Efficient%20Fine-Tuning,%20Semi-Supervised%20Fine-Tuning-orange) ![img](https://img.shields.io/badge/-Natural%20Language-lightgrey) ![img](https://img.shields.io/badge/Chat-green)

  *Canwen Xu, Daya Guo, Nan Duan, Julian McAuley*.


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
