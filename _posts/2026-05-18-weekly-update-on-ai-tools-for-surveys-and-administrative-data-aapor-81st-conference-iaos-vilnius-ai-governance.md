---
layout: post
title: "AAPOR 81st Conference, IAOS Vilnius, and AI Governance in Official Statistics"
date: 2026-05-18
author: Dramane Bako
description: "The AAPOR 81st Annual Conference underscored the cautious integration of LLMs in survey research, emphasizing responsible frameworks for translation..."
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, official-statistics, administrative-data]
lang: en
---

## 🇬🇧 English


Coverage period: May 11–18, 2026  
Keywords: AI tools, surveys, administrative data, large language models, official statistics, AI governance, survey methodology, machine learning, data quality

## **Key Takeaways**

- The AAPOR 81st Annual Conference underscored the cautious integration of LLMs in survey research, emphasizing responsible frameworks for translation, analysis, and voice-based surveys.  
- IAOS 2026 highlighted AI’s transformative potential in official statistics, with significant focus on AI governance, responsible use, and broad international collaboration.  
- The IFPRI blog signaled persistent data infrastructure gaps in low-income countries limiting the benefits of AI for development research, advocating sustained investment in foundational survey systems.  
- The arXiv paper on Survey-aware Machine Learning (SaML) introduced a rigorous nine-step framework for valid population inference from complex survey data, addressing common biases in ML applications.  
- The Kenya AI means-testing investigation revealed critical risks of relying solely on proxy-based ML models for high-stakes administrative decisions, emphasizing the irreplaceable value of direct survey data.  
- Recent scholarship in Nature called for new oversight frameworks tailored to the unique challenges posed by LLMs, underscoring gaps in current regulatory models relevant to official statistics uses.

---

## **AAPOR 81st Annual Conference: Responsible AI Integration in Survey Research**

The American Association for Public Opinion Research convened its 81st Annual Conference in Los Angeles, advancing discourse on AI integration in survey methodology. A highlight was the release of the Task Force Report "Responsible AI Integration in Survey Research" (Rothschild et al., 2026), which offers a comprehensive framework for deploying large language models (LLMs) as AI interviewers. The report addresses critical survey components including questionnaire translation accuracy, complex survey data analysis workflows, and novel voice-based survey modalities, thereby setting a foundation for ethical and methodologically sound AI adoption.

AAPOR presentations reflected a balance of optimism and caution regarding LLMs. The U.S. Census Bureau exhibited promising applications of LLMs, while Westat researchers shared advancements integrating machine learning within survey methodology. Conversely, findings from the University of Michigan’s Center for Political Studies challenged exaggerated expectations, reporting that LLMs currently fall short of substituting survey respondents for data imputation tasks. This nuanced perspective tempers expectations and highlights the ongoing need for methodological rigor.

The conference also hosted a session led by the UN Statistics Division focusing on citizen and participatory data, reframing data quality discussions in the context of AI-enhanced data streams. Demonstrations from NORC, SSRS, and Prolific underscored AI-powered quality assurance methods, illustrating industry advancements in real-time data validation and anomaly detection. Together, these contributions emphasize responsible, transparent AI practices embedded in traditional survey research footprints.

| **AAPOR Task Force Report Highlights**                 | **Description**                                                  |
|--------------------------------------------------------|----------------------------------------------------------------|
| Questionnaire Translation                              | Use of LLMs to enhance linguistic accuracy and cultural context|
| Complex Data Analysis                                  | Integration of LLMs with weighted and multi-stage survey data  |
| Voice-based Survey Modalities                          | Deployment of speech recognition and LLM-generated interviewing|
| Ethical Framework                                     | Guidelines for transparency, bias mitigation, and informed consent|
| Validation & Monitoring                                | Ongoing assessment of AI interviewer performance and fairness  |

---

## **IAOS 2026 Conference: AI Governance and Official Statistics Transformation**

The 20th IAOS Conference in Vilnius gathered officials and statisticians from over 100 countries under the theme "Data Revolution: Reshaping Official Statistics." The conference foregrounded AI governance, with May 11 short courses equipping participants on responsible AI use tailored for official statistics production. This educational component emphasized frameworks and policy considerations, reflecting growing awareness of AI challenges such as algorithmic transparency, bias, and accountability.

Participants from national statistical offices shared numerous use cases where AI enhances data collection, processing, and dissemination. Discussions highlighted advanced AI applications streamlining administrative data integration and automated classification. Nonetheless, speakers consistently pointed to the need for robust governance mechanisms to ensure ethical, equitable, and high-quality outputs consistent with international statistical standards.

The IAOS forum also fostered dialogue on cross-border cooperation to tackle AI-related challenges. This included harmonizing AI regulatory approaches and developing capacity-building programs to improve AI literacy among statisticians worldwide. The emphasis on governance and collaborative stewardship signals a pragmatic shift from mere technological adoption to embedding AI within resilient statistical systems.

---

## **Development Research and AI: Insights from IFPRI’s May 13 Blog**

The International Food Policy Research Institute (IFPRI) underscored in a recent blog that AI’s strength in pattern recognition is constrained by its limited understanding of contextual realities, necessitating robust, high-quality data inputs. Co-authors Kalle Hirvonen and Jessica Leight argue that data scarcity in low-income countries remains a critical bottleneck for AI-driven insights, especially in development contexts where informal economies are poorly documented.

This reality challenges enthusiasm for AI as a transformative tool in poverty and agricultural statistics. The authors caution that remotely sensed data or phone surveys can complement but not replace in-person household surveys, which remain the gold standard. Crucially, they advocate increased donor and government investment in national statistics systems (e.g., LSMS, DHS) and local researcher capacity to optimize AI’s utility.

The blog also highlights the Project APE initiative at the University of Zurich, illustrating that despite AI’s autonomy in generating economic papers, human researchers continue to outperform AI in quality assessments. Moreover, the concentration of AI research in data-rich environments risks exacerbating geographic and thematic disparities in development research, a concern for equitable knowledge production.

---

## **Survey-aware Machine Learning (SaML): Addressing Bias and Validity in Health Data**

An arXiv preprint (Oh et al., 2026) advances methodological rigor in applying ML to complex health surveys by detailing Survey-aware Machine Learning (SaML). The paper identifies a prevalent pitfall: many ML models neglect critical survey design features such as primary sampling units, stratification, and sampling weights, leading to biased estimation and deficits in population-level generalizability.

The authors propose a nine-step guideline to systematically integrate survey metadata into all modeling stages. This includes design-based weighting during model training, specialized cross-validation schemes accounting for sampling designs, and survey-adjusted evaluation metrics to ensure fairness and validity. Their approach bridges classical survey methodology with modern ML, promoting responsible analytics for health and population inference.

| **Survey-aware Machine Learning (SaML) Nine Steps**      | **Purpose and Description**                                   |
|----------------------------------------------------------|---------------------------------------------------------------|
| 1. Define survey design parameters                        | Identify PSUs, strata, and weights                             |
| 2. Preprocess data respecting design                      | Adjust variable distributions and missingness                 |
| 3. Weighting scheme integration                            | Incorporate sampling weights into training loss functions      |
| 4. Model specification considering design features        | Choose algorithms compatible with survey complexities         |
| 5. Design-based cross-validation                           | Validate with sampling units and strata preserved              |
| 6. Hyperparameter tuning aware of survey design            | Optimize parameters using survey-stratified folds              |
| 7. Performance evaluation adjusted for sampling            | Use design-consistent metrics (e.g., weighted RMSE)            |
| 8. Fairness assessments at population level                | Measure equity across demographic subgroups                    |
| 9. Reporting and transparency                              | Document survey integration methods and potential biases       |

SaML’s comprehensive checklist offers a valuable operational tool, especially for official statisticians and researchers integrating ML into survey data workflows.

---

## **AI in Administrative Data: Lessons from Kenya’s Means-Testing Investigation**

Investigative reporting by Lighthouse Reports, The Guardian, and Africa Uncensored brought to light flaws in Kenya’s Social Health Authority (SHA) AI-based means-testing algorithm. The model, which predicts household income from 43 proxy variables, systematically imposed higher healthcare costs on the poorest citizens due to biased model design and proxy limitations.

This case exposes critical dangers when algorithms trained on proxy indicators substitute for direct, carefully collected survey data — particularly in social protection applications with substantial equity implications. The findings highlight the indispensable role of transparent, survey-grounded validation and continuous monitoring of AI systems deployed in administrative contexts.

For the survey research community, this investigation serves as a cautionary tale reinforcing that algorithmic proxies cannot yet replace rigorous household survey data, especially in vulnerable populations and complex social settings. It calls for enhanced model governance, fairness auditing, and inclusive design involving domain experts and affected communities.

---

## **LLM Oversight: Emerging Regulatory Frameworks in Official Statistics**

A recent article in npj Digital Medicine (published May 15, 2026) proposes a novel taxonomy and monitoring framework for large language models, emphasizing the insufficiency of existing regulatory approaches given their generative, probabilistic characteristics. The paper lays out multiple dimensions of LLM capability (e.g., factuality, bias, interpretability), monitoring metrics, and governance considerations necessary for responsible deployment.

This work directly informs the official statistics domain, where LLMs are increasingly explored for tasks ranging from questionnaire design support to automated data processing. The proposed governance framework advocates continuous oversight mechanisms, incorporating transparent auditing, human-in-the-loop controls, and ethical accountability structures.

Aligning with AAPOR’s responsible AI guidelines, this emerging scholarship offers practical policy roadmaps to anticipate and mitigate unique risks posed by LLMs in data collection and dissemination, ensuring trust and reliability in official statistics.

---

---

## **IAOS 2026 Session: AI & ML in Official Statistics — Key Insights**

The IAOS 2026 conference session on "AI & ML in Official Statistics (1)" was held on Tuesday, 12 May 2026, from 4:30 p.m. to 6 p.m. in the ZETA 2 room in Vilnius, Lithuania. Chaired by Dominik Rozkrut, the session explored the transformative potential of Artificial Intelligence (AI) and Machine Learning (ML) technologies across various facets of official statistics. Highlighting innovations from digital twins and decision support systems to AI-driven data collection and hierarchical classification, the session addressed critical challenges including organizational readiness, transparency, and the integration of heterogeneous data sources. The presentations collectively illustrated advanced AI methodologies applied to survey methodology and administrative data, with direct implications for improving timeliness, accuracy, and usability of statistical outputs.

### 7.1 Digital Statistical Twins: The Virtual Hungary Project  
*Author: Dr Ákos Jakobi (Hungarian Central Statistical Office)*

The Virtual Hungary initiative exemplifies a pioneering effort to create a digital statistical twin integrating diverse administrative and survey datasets at an unprecedented granularity. By constructing a synthetic, nationwide socio-economic information system that links individual-level data across domains such as demographics, tax, and corporate records, the project represents a significant advance in the ability to derive quasi real-time insights into the state of the economy and society. This integrative approach not only facilitates the creation of cross-domain indicators but also enables flexible aggregation, supporting analysis from micro to macro levels—all while maintaining strict anonymity safeguards essential for statistical confidentiality.

From a methodological perspective, the project’s automated imputation techniques demonstrate how AI can alleviate common challenges linked to missing or inconsistent data in administrative sources, thereby enhancing data quality and reducing respondent burden often associated with traditional surveys. For survey statisticians, this digital twin framework opens avenues for more efficient data collection strategies and hybrid data models that combine survey and administrative records. Furthermore, the capacity to examine interlinked variables across previously siloed datasets supports richer causal inference and nuanced policy evaluation, heralding a shift towards dynamic, data-driven policymaking grounded in comprehensive statistical evidence.

### 7.2 AI-Enabled Decision Support for National Statistical Offices: A Framework for Transparent and Explainable Statistical Intelligence  
*Author: Ms Amena Alzaabi (Statistics Centre – Abu Dhabi, SCAD)*

Alzaabi’s presentation introduced an AI-driven decision support framework leveraging large language models (LLMs) to create natural-language interfaces for querying complex statistical repositories. This approach shifts away from classical static dissemination formats—such as tables and dashboards—toward interactive, user-friendly systems capable of generating tailored insights on-demand. A core strength of this framework lies in its embedding of explainability mechanisms, aligning with eXplainable AI (XAI) principles by transparently linking AI-generated outputs back to source data, underlying classifications, and methodological notes.

For the domain of surveys and administrative data, this model addresses major barriers related to data accessibility and comprehension by policymakers and analysts who may lack advanced technical skills. The integration of confidentiality safeguards through controlled access to pre-approved statistical layers also ensures compliance with data-protection mandates, which is critical when AI interfaces interact with sensitive or granular datasets. By democratizing access to complex, multi-domain data environments and lowering cognitive load, this framework promises to enhance the real-world impact of official statistics on policy and decision-making processes.

### 7.3 Role of Artificial Intelligence in Collecting Foreign Trade Data: Opportunities, Challenges, and Application Potential  
*Author: Mr Mostafa Mahmoud Abdelnaby Esmail (NCAPMAS, Egypt)*

Esmail’s investigation focuses on AI’s expanding role in the collection and processing of foreign trade data, an area traditionally challenged by timeliness, data quality, and manual processing errors. By reviewing international experiences and practical applications, the study highlights how AI techniques—such as automated data extraction, anomaly detection, and predictive analytics—can enhance the accuracy and efficiency of trade statistics. The potential for AI to expedite workflows and minimize human error is particularly relevant for statistical offices that contend with high volumes of detailed transaction data sourced from multiple customs, shipping, and commercial records.

The report underscores, however, that successful AI integration in foreign trade data collection hinges on critical enablers: robust digital infrastructure, capacity building for skilled personnel, and supportive regulatory frameworks. This aligns with broader challenges faced in administrative data usage, where data heterogeneity and privacy concerns require coordinated institutional change. For official statisticians, these insights reinforce the necessity of progressive investment in AI competencies and infrastructure to fully leverage new technologies for complex data environments, while maintaining statistical rigor and trustworthiness.

### 7.4 An Agent-Based LLM Framework for Automatic Labeling in Hierarchical Statistical Nomenclatures  
*Author: Mr Theo Ferry (INSEE, France)*

Ferry presented GRAAL, a novel agent-based framework integrating Large Language Models with graph-based representations of hierarchical statistical classifications (e.g., NACE, COICOP). This approach addresses persistent challenges of supervised learning in hierarchical classification tasks such as limited labeled data, inconsistency, and lack of explainability. By representing classifications as knowledge graphs and deploying multi-agent navigation and reasoning agents, the framework enables consistent, traceable, and explainable automatic labeling of statistical units while enforcing taxonomic rules.

The implications for administrative data coding and survey metadata classification are considerable. Automated, consistent labeling supported by explainable AI agents reduces the reliance on costly manual annotation by domain experts and enhances the auditability of classification decisions—an essential feature for official statistics quality control and user confidence. Furthermore, GRAAL’s capacity to generate synthetic labeled data can facilitate the training of downstream AI models, thereby addressing data scarcity issues common in official classification systems. This agent-based, knowledge-structured paradigm represents a promising pathway to modernize the handling of complex nomenclatures central to survey design and data integration processes.

---

| Paper Title                                                                 | Author / Institution                   | Core AI Approach                                | Key Implication for Official Statistics                                    |
|-----------------------------------------------------------------------------|--------------------------------------|------------------------------------------------|---------------------------------------------------------------------------|
| Potentials of a Digital Statistical Twin: the Virtual Hungary Project       | Dr Ákos Jakobi / Hungarian CSO       | Integrated synthetic data system with AI-driven imputation | Enhanced micro-level data integration enabling quasi real-time policymaking |
| AI-Enabled Decision Support for National Statistical Offices                | Ms Amena Alzaabi / SCAD              | Large Language Models (LLMs) with explainable AI for natural language interaction | Lowers technical barriers; transparent, explainable AI for interactive data access |
| Role of Artificial Intelligence in Collecting Foreign Trade Data            | Mr Mostafa Mahmoud Abdelnaby Esmail / NCAPMAS Egypt | AI analytics for automated data collection, error reduction | Improved data quality and processing speed; need for supportive infrastructure and governance |
| An Agent-Based LLM Framework for Automatic Labeling in Hierarchical Nomenclatures | Mr Theo Ferry / INSEE, France        | Agent-based reasoning over knowledge graphs with LLMs | Consistent, explainable, and scalable classification automation             |

---

This session underscored several cross-cutting themes essential for the future landscape of official statistics. A prominent motif was the strategic integration of AI techniques to enhance data linkage, quality, and usability, particularly through innovative synthetic systems like digital statistical twins and multi-agent classification frameworks. Transparency and explainability emerged as critical principles, ensuring AI outputs remain interpretable, trustworthy, and aligned with established statistical standards. Equally, organizational readiness—including digital infrastructure, skilled personnel, and appropriate regulatory environments—was highlighted as a prerequisite for successful AI adoption. Collectively, these advances promise to transform survey methodology and administrative data processing into more agile, user-centric, and policy-relevant functions, reinforcing the vital role of official statistics in an increasingly complex data ecosystem.

### Looking Ahead

In the coming months, the emphasis will continue to shift toward strengthening governance architectures underpinning AI integration in surveys and administrative data. The upcoming UNECE task force on AI ethics and the forthcoming international standards on AI transparency will likely build upon insights from AAPOR and IAOS engagements.

Further methodological work is expected to refine frameworks like Survey-aware Machine Learning, extending beyond health surveys to encompass agricultural and socio-economic domains, which are pivotal to FAO’s mandate. Simultaneously, pilot initiatives testing ethical AI interviewers in multilingual, multi-modal survey environments may emerge, leveraging learnings from the AAPOR Task Force.

On the global development front, the reiteration of investment needs in foundational surveys and local research capacity from IFPRI’s report signals potential advocacy avenues to enhance FAO’s collaboration with national statistics systems. Addressing data poverty remains a prerequisite for responsible AI application and unbiased decision-making.

Continuous monitoring of deployed AI systems in administrative settings, informed by cautionary cases like Kenya’s means-testing, will remain critical. This entails collaborating with partners on fairness audits and refining practices to prevent unintended harms.

---

*This weekly monitoring series synthesizes the evolving landscape of AI tools in surveys and administrative data, supporting informed decision making and fostering methodological innovation within official statistics and international data communities.*

---

## 🇫🇷 Français

**Mise à jour hebdomadaire sur les outils d’IA pour les enquêtes et les données administratives : 81e conférence AAPOR, IAOS Vilnius et gouvernance de l’IA dans les statistiques officielles**

Période couverte : 11–18 mai 2026  
Mots-clés : outils d’IA, enquêtes, données administratives, grands modèles de langage, statistiques officielles, gouvernance de l’IA, méthodologie d’enquête, apprentissage automatique, qualité des données

### Points clés

- La 81e conférence annuelle de l’AAPOR a souligné l’intégration prudente des LLM dans la recherche par sondage, en insistant sur des cadres responsables pour la traduction, l’analyse et les enquêtes vocales.  
- L’IAOS 2026 a mis en lumière le potentiel transformateur de l’IA dans les statistiques officielles, avec un accent important sur la gouvernance de l’IA, son usage responsable et une large collaboration internationale.  
- Le blog de l’IFPRI a indiqué que les lacunes persistantes dans les infrastructures de données dans les pays à faible revenu limitent les bénéfices de l’IA pour la recherche en développement, plaidant pour un investissement soutenu dans les systèmes d’enquêtes fondamentaux.  
- L’article arXiv sur le Survey-aware Machine Learning (SaML) a présenté un cadre rigoureux en neuf étapes pour une inférence populationnelle valide à partir de données d’enquêtes complexes, traitant les biais courants dans les applications ML.  
- L’enquête sur les tests de moyens basés sur l’IA au Kenya a révélé des risques critiques liés à la dépendance exclusive aux modèles ML basés sur des proxys pour des décisions administratives à fort enjeu, soulignant la valeur irremplaçable des données issues d’enquêtes directes.  
- Des travaux récents publiés dans Nature appellent à de nouveaux cadres de surveillance adaptés aux défis spécifiques posés par les LLM, mettant en évidence des lacunes dans les modèles réglementaires actuels pertinents pour les usages en statistiques officielles.

---

## **81e conférence annuelle de l’AAPOR : Intégration responsable de l’IA dans la recherche par sondage**

L’American Association for Public Opinion Research a tenu sa 81e conférence annuelle à Los Angeles, faisant progresser le débat sur l’intégration de l’IA dans la méthodologie des enquêtes. Un moment fort a été la publication du rapport du groupe de travail « Responsible AI Integration in Survey Research » (Rothschild et al., 2026), qui propose un cadre complet pour déployer les grands modèles de langage (LLM) comme intervieweurs IA. Le rapport aborde des composantes essentielles des enquêtes telles que la précision de la traduction des questionnaires, les flux d’analyse des données complexes et les modalités innovantes d’enquêtes vocales, posant ainsi les bases d’une adoption éthique et méthodologiquement solide de l’IA.

Les présentations à l’AAPOR ont fait preuve d’un équilibre entre optimisme et prudence à l’égard des LLM. Le U.S. Census Bureau a présenté des applications prometteuses des LLM, tandis que les chercheurs de Westat ont partagé des avancées d’intégration de l’apprentissage automatique dans la méthodologie d’enquête. En revanche, les résultats du Center for Political Studies de l’Université du Michigan ont tempéré les attentes exagérées, rapportant que les LLM ne peuvent actuellement pas remplacer les répondants aux enquêtes pour les tâches d’imputation des données. Cette perspective nuancée modère les attentes et souligne la nécessité constante de rigueur méthodologique.

La conférence a également accueilli une session dirigée par la Division des Statistiques des Nations Unies centrée sur les données citoyennes et participatives, repositionnant les discussions sur la qualité des données dans le contexte des flux de données amplifiés par l’IA. Des démonstrations de NORC, SSRS et Prolific ont mis en avant des méthodes d’assurance qualité assistées par l’IA, illustrant les progrès industriels dans la validation en temps réel et la détection d’anomalies. Ces contributions insistent sur des pratiques d’IA responsables et transparentes, intégrées au cadre traditionnel de la recherche par sondage.

| **Points forts du rapport du groupe de travail AAPOR**             | **Description**                                                  |
|--------------------------------------------------------------------|-----------------------------------------------------------------|
| Traduction des questionnaires                                      | Utilisation des LLM pour améliorer la précision linguistique et le contexte culturel |
| Analyse complexe des données                                       | Intégration des LLM aux données d’enquêtes pondérées et à plusieurs niveaux |
| Modalités d’enquête vocales                                        | Déploiement de la reconnaissance vocale et d’entretiens générés par LLM |
| Cadre éthique                                                     | Directives pour la transparence, la mitigation des biais et le consentement éclairé |
| Validation & Suivi                                                | Évaluation continue de la performance et de l’équité des intervieweurs IA |

---

## **Conférence IAOS 2026 : Gouvernance de l’IA et transformation des statistiques officielles**

La 20e conférence IAOS à Vilnius a réuni des responsables et statisticiens de plus de 100 pays sous le thème « Révolution des données : remodeler les statistiques officielles ». La conférence a mis en avant la gouvernance de l’IA, avec des cours courts le 11 mai destinés à équiper les participants à une utilisation responsable de l’IA adaptée à la production de statistiques officielles. Cette composante pédagogique a insisté sur les cadres et considérations politiques, témoignant d’une prise de conscience grandissante des défis liés à l’IA tels que la transparence algorithmique, les biais et la responsabilité.

Des représentants de bureaux nationaux de statistiques ont partagé de nombreux cas d’usage où l’IA améliore la collecte, le traitement et la diffusion des données. Les discussions ont mis en lumière des applications avancées d’IA facilitant l’intégration des données administratives et la classification automatisée. Néanmoins, les intervenants ont constamment souligné la nécessité de mécanismes de gouvernance robustes pour garantir des résultats éthiques, équitables et de haute qualité, conformes aux normes statistiques internationales.

Le forum IAOS a également favorisé le dialogue sur la coopération transfrontalière pour relever les défis liés à l’IA. Cela comprenait l’harmonisation des approches réglementaires et le développement de programmes de renforcement des capacités pour améliorer la littératie en IA chez les statisticiens dans le monde. L’accent mis sur la gouvernance et la responsabilité collaborative traduit un passage pragmatique d’une simple adoption technologique à une intégration de l’IA dans des systèmes statistiques résilients.

---

## **Recherche en développement et IA : enseignements du blog de l’IFPRI du 13 mai**

L’International Food Policy Research Institute (IFPRI) a souligné dans un blog récent que la force de l’IA en reconnaissance de motifs est limitée par sa compréhension restreinte des réalités contextuelles, nécessitant des données robustes et de haute qualité. Les coauteurs Kalle Hirvonen et Jessica Leight affirment que la rareté des données dans les pays à faible revenu reste un goulot d’étranglement critique pour les analyses basées sur l’IA, surtout dans les contextes de développement où les économies informelles sont peu documentées.

Cette réalité tempère l’enthousiasme pour l’IA comme outil transformateur dans les statistiques de la pauvreté et de l’agriculture. Les auteurs mettent en garde contre le fait que les données issues de la télédétection ou des enquêtes téléphoniques peuvent compléter mais ne remplacent pas les enquêtes de terrain auprès des ménages, qui restent la référence. Ils plaident en particulier pour un accroissement des investissements des bailleurs et gouvernements dans les systèmes statistiques nationaux (e.g., LSMS, DHS) et la capacité locale des chercheurs afin d’optimiser l’utilité de l’IA.

Le blog met également en avant l’initiative Project APE de l’Université de Zurich, illustrant que malgré l’autonomie de l’IA à générer des articles économiques, les chercheurs humains continuent de surpasser l’IA dans les évaluations qualitatives. De plus, la concentration de la recherche en IA dans des environnements riches en données risque d’accentuer les disparités géographiques et thématiques en recherche sur le développement, ce qui soulève des inquiétudes en matière de production équitable de connaissances.

---

## **Survey-aware Machine Learning (SaML) : traiter biais et validité dans les données sanitaires**

Un preprint arXiv (Oh et al., 2026) fait progresser la rigueur méthodologique de l’application du ML aux enquêtes sanitaires complexes en détaillant le Survey-aware Machine Learning (SaML). L’article identifie une erreur répandue : beaucoup de modèles ML négligent les caractéristiques essentielles du design d’enquête, telles que les unités primaires d’échantillonnage, la stratification et les poids d’échantillonnage, conduisant à des estimations biaisées et une généralisation insuffisante au niveau populationnel.

Les auteurs proposent un guide en neuf étapes pour intégrer systématiquement les métadonnées d’enquête à toutes les phases de modélisation. Cela comprend la pondération basée sur le design lors de l’entraînement, des schémas de validation croisée tenant compte des structures d’échantillonnage, et des métriques d’évaluation ajustées aux enquêtes pour garantir équité et validité. Cette approche relie la méthodologie classique des enquêtes avec le ML moderne, promouvant une analyse responsable pour l’inférence en santé et population.

| **Neuf étapes de Survey-aware Machine Learning (SaML)**           | **But et description**                                         |
|-------------------------------------------------------------------|---------------------------------------------------------------|
| 1. Définir les paramètres du design d’enquête                     | Identifier les unités primaires d’échantillonnage (UPS), strates et poids |
| 2. Prétraiter les données en respectant le design                  | Ajuster les distributions des variables et la gestion des valeurs manquantes |
| 3. Intégration des poids d’échantillonnage                         | Incorporer les poids dans la fonction de perte durant l’entraînement |
| 4. Spécification du modèle tenant compte des caractéristiques du design | Choisir des algorithmes compatibles avec la complexité des enquêtes |
| 5. Validation croisée basée sur le design                           | Valider en préservant les unités d’échantillonnage et les strates |
| 6. Réglage des hyperparamètres conscient du design                 | Optimiser avec des plis stratifiés selon le design             |
| 7. Évaluation des performances ajustée à l’échantillonnage        | Utiliser des métriques cohérentes au design (ex. RMSE pondéré)  |
| 8. Évaluations d’équité au niveau populationnel                    | Mesurer l’équité entre sous-groupes démographiques              |
| 9. Rapport et transparence                                         | Documenter méthodes d’intégration du design et biais potentiels |

La checklist exhaustive de SaML constitue un outil opérationnel précieux, notamment pour les statisticiens officiels et chercheurs intégrant le ML aux flux de données d’enquête.

---

## **L’IA dans les données administratives : enseignements de l’enquête sur les tests de moyens au Kenya**

Des enquêtes journalistiques de Lighthouse Reports, The Guardian, et Africa Uncensored ont révélé des défauts dans l’algorithme de test de moyens basé sur l’IA de la Social Health Authority (SHA) du Kenya. Le modèle, qui prédit le revenu des ménages à partir de 43 variables proxy, a imposé systématiquement des coûts de santé plus élevés aux citoyens les plus pauvres en raison d’un biais dans la conception du modèle et des limites des proxys.

Ce cas met en lumière les dangers critiques que représentent les algorithmes entraînés sur des indicateurs proxy substituant les données directes minutieusement collectées par enquête, notamment dans des applications de protection sociale aux fortes implications en termes d’équité. Les résultats soulignent le rôle indispensable d’une validation transparente, fondée sur des enquêtes, ainsi que d’un suivi continu des systèmes IA déployés en contexte administratif.

Pour la communauté de la recherche par sondage, cette enquête sert de mise en garde, rappelant que les proxys algorithmiques ne remplacent pas encore les données rigoureuses des enquêtes auprès des ménages, surtout dans les populations vulnérables et environnements sociaux complexes. Elle appelle à un renforcement de la gouvernance des modèles, des audits d’équité et une conception inclusive impliquant experts métier et communautés concernées.

---

## **Surveillance des LLM : cadres réglementaires émergents en statistiques officielles**

Un article récent dans npj Digital Medicine (publié le 15 mai 2026) propose une nouvelle taxonomie et un cadre de suivi pour les grands modèles de langage, soulignant l’insuffisance des approches réglementaires actuelles au regard de leurs caractéristiques génératives et probabilistes. L’article expose plusieurs dimensions des capacités des LLM (e.g., factualité, biais, interprétabilité), des métriques de suivi, et des considérations de gouvernance nécessaires à un déploiement responsable.

Ce travail a un impact direct pour le domaine des statistiques officielles, où les LLM sont de plus en plus explorés pour des tâches allant du soutien à la conception de questionnaires au traitement automatisé des données. Le cadre de gouvernance proposé préconise des mécanismes de surveillance continue, intégrant des audits transparents, le contrôle humain dans la boucle, et des structures de responsabilité éthique.

S’alignant avec les directives responsables en IA de l’AAPOR, cette recherche émergente offre des feuilles de route politiques pragmatiques pour anticiper et mitiger les risques uniques posés par les LLM dans la collecte et la diffusion des données, assurant confiance et fi


## **Session IAOS 2026 : IA & ML en statistiques officielles — Principaux enseignements**

La session de la conférence IAOS 2026 intitulée « AI & ML in Official Statistics (1) » s’est tenue le mardi 12 mai 2026, de 16h30 à 18h, dans la salle ZETA 2 à Vilnius, Lituanie. Animée par Dominik Rozkrut, la session a exploré le potentiel transformateur des technologies d’Intelligence Artificielle (IA) et de Machine Learning (ML) dans divers aspects des statistiques officielles. Mettant en lumière des innovations allant des jumeaux numériques et systèmes d’aide à la décision à la collecte de données pilotée par IA ainsi que la classification hiérarchique, la session a abordé des défis cruciaux tels que la préparation organisationnelle, la transparence et l’intégration de sources de données hétérogènes. Les présentations ont illustré collectivement des méthodologies avancées d’IA appliquées à la méthodologie des enquêtes et aux données administratives, avec des implications directes pour améliorer la rapidité, la précision et l’utilisabilité des résultats statistiques.

### 7.1 Jumeaux statistiques numériques : Le projet Virtual Hungary  
*Auteur : Dr Ákos Jakobi (Hungarian Central Statistical Office)*

L’initiative Virtual Hungary illustre un effort pionnier pour créer un jumeau statistique numérique intégrant divers jeux de données administratives et d’enquêtes à une granularité sans précédent. En construisant un système synthétique d’information socio-économique à l’échelle nationale reliant des données individuelles issues de domaines tels que la démographie, la fiscalité et les registres d’entreprise, le projet représente une avancée significative dans la capacité à obtenir des perspectives quasi temps réel sur l’état de l’économie et de la société. Cette approche intégrative facilite non seulement la création d’indicateurs croisés entre domaines, mais permet également une agrégation flexible, appuyant l’analyse du micro au macro niveau — tout en maintenant des protections strictes d’anonymat essentielles pour la confidentialité statistique.

D’un point de vue méthodologique, les techniques d’imputation automatisées du projet démontrent comment l’IA peut alléger les défis fréquents liés aux données manquantes ou incohérentes dans les sources administratives, améliorant ainsi la qualité des données et réduisant la charge des répondants souvent associée aux enquêtes traditionnelles. Pour les statisticiens d’enquête, ce cadre de jumeau numérique ouvre des pistes pour des stratégies de collecte de données plus efficaces et des modèles hybrides combinant données d’enquête et administratives. De plus, la capacité à examiner des variables interconnectées à travers des jeux de données autrefois cloisonnés soutient une inférence causale plus riche et une évaluation politique nuancée, annonçant un virage vers une politique dynamique et basée sur des données, fondée sur des preuves statistiques complètes.

### 7.2 Soutien à la décision par IA pour les Offices statistiques nationaux : Un cadre pour une intelligence statistique transparente et explicable  
*Auteur : Mme Amena Alzaabi (Statistics Centre – Abu Dhabi, SCAD)*

La présentation d’Alzaabi a introduit un cadre de soutien à la décision piloté par IA utilisant de grands modèles de langage (LLM) pour créer des interfaces en langage naturel permettant d’interroger des répertoires statistiques complexes. Cette approche rompt avec les formats classiques de diffusion statique — tels que tableaux et tableaux de bord — pour offrir des systèmes interactifs et conviviaux capables de générer des insights personnalisés à la demande. La force principale de ce cadre réside dans l’intégration de mécanismes d’explicabilité, conformes aux principes de l’eXplainable AI (XAI), en reliant de manière transparente les résultats générés par l’IA aux données sources, classifications sous-jacentes et notes méthodologiques.

Pour le domaine des enquêtes et des données administratives, ce modèle répond aux principaux obstacles liés à l’accessibilité et à la compréhension des données par les décideurs et analystes qui peuvent manquer de compétences techniques avancées. L’intégration de garanties de confidentialité via un accès contrôlé à des couches statistiques préapprouvées assure également le respect des normes de protection des données, ce qui est crucial lorsque des interfaces IA manipulent des données sensibles ou granulaires. En démocratisant l’accès à des environnements de données complexes et multi-domaines tout en réduisant la charge cognitive, ce cadre promet d’accroître l’impact concret des statistiques officielles sur les processus de politique publique et de prise de décision.

### 7.3 Rôle de l’intelligence artificielle dans la collecte des données du commerce extérieur : opportunités, défis et potentiel d’application  
*Auteur : M. Mostafa Mahmoud Abdelnaby Esmail (NCAPMAS, Égypte)*

L’investigation d’Esmail porte sur le rôle croissant de l’IA dans la collecte et le traitement des données du commerce extérieur, un domaine traditionnellement confronté à des enjeux de rapidité, qualité des données et erreurs de traitement manuel. En analysant des expériences internationales et des applications pratiques, l’étude met en lumière comment les techniques d’IA — telles que l’extraction automatisée de données, la détection d’anomalies et l’analyse prédictive — peuvent améliorer la précision et l’efficacité des statistiques commerciales. Le potentiel de l’IA pour accélérer les flux de travail et minimiser l’erreur humaine est particulièrement pertinent pour les offices statistiques qui traitent de grands volumes de données transactionnelles détaillées provenant de multiples registres douaniers, maritimes et commerciaux.

Le rapport souligne toutefois que la réussite de l’intégration de l’IA dans la collecte des données du commerce extérieur repose sur des facteurs clés : une infrastructure numérique robuste, le renforcement des compétences du personnel qualifié et des cadres réglementaires favorables. Cela rejoint les défis plus larges rencontrés dans l’usage des données administratives, où l’hétérogénéité des données et les préoccupations relatives à la confidentialité nécessitent un changement institutionnel coordonné. Pour les statisticiens officiels, ces enseignements réaffirment la nécessité d’investissements progressifs dans les compétences et infrastructures en IA afin de tirer pleinement parti des nouvelles technologies dans des environnements de données complexes, tout en maintenant la rigueur et la fiabilité statistiques.

### 7.4 Un cadre agentiel basé sur LLM pour l’étiquetage automatique dans les nomenclatures statistiques hiérarchiques  
*Auteur : M. Theo Ferry (INSEE, France)*

Ferry a présenté GRAAL, un nouveau cadre agentiel intégrant de grands modèles de langage avec des représentations graphiques des classifications statistiques hiérarchiques (ex. NACE, COICOP). Cette approche répond aux défis persistants de l’apprentissage supervisé dans les tâches de classification hiérarchique tels que la limitation des données étiquetées, l’incohérence et le manque d’explicabilité. En représentant les classifications sous forme de graphes de connaissances et en déployant des agents à navigation et raisonnement multi-agents, le cadre permet un étiquetage automatique cohérent, traçable et explicable des unités statistiques tout en respectant les règles taxonomiques.

Les implications pour le codage des données administratives et la classification des métadonnées d’enquête sont considérables. L’étiquetage automatisé et cohérent soutenu par des agents d’IA explicable réduit la dépendance à l’annotation manuelle coûteuse effectuée par des experts métiers et améliore l’auditabilité des décisions de classification — une caractéristique essentielle pour le contrôle qualité et la confiance des utilisateurs en statistiques officielles. De plus, la capacité de GRAAL à générer des données étiquetées synthétiques peut faciliter la formation des modèles IA en aval, répondant ainsi aux problèmes de rareté des données fréquents dans les systèmes de classification officiels. Ce paradigme agentiel structuré par la connaissance représente une voie prometteuse pour moderniser la gestion des nomenclatures complexes, centrales dans la conception des enquêtes et les processus d’intégration des données.

---

| Titre de l’article                                                            | Auteur / Institution                 | Approche IA principale                          | Implication clé pour les statistiques officielles                             |
|-------------------------------------------------------------------------------|------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------|
| Potentials of a Digital Statistical Twin: the Virtual Hungary Project         | Dr Ákos Jakobi / Hungarian CSO     | Système de données synthétiques intégrées avec imputation pilotée par IA | Intégration accrue des données micro permettant une prise de décision quasi temps réel |
| AI-Enabled Decision Support for National Statistical Offices                  | Mme Amena Alzaabi / SCAD            | Grands modèles de langage (LLM) avec IA explicable pour interaction en langage naturel | Baisse des barrières techniques ; IA transparente et explicable pour un accès interactif aux données |
| Role of Artificial Intelligence in Collecting Foreign Trade Data              | M. Mostafa Mahmoud Abdelnaby Esmail / NCAPMAS Égypte | Analyse IA pour collecte automatisée, réduction des erreurs         | Amélioration de la qualité et de la vitesse de traitement des données ; besoin d’infrastructures et gouvernance adaptées |
| An Agent-Based LLM Framework for Automatic Labeling in Hierarchical Nomenclatures | M. Theo Ferry / INSEE, France      | Raisonnement agentiel sur graphes de connaissances avec LLMs       | Automatisation cohérente, explicable et évolutive de la classification       |

---

Cette session a souligné plusieurs thèmes transversaux essentiels pour le futur des statistiques officielles. Un motif récurrent a été l’intégration stratégique des techniques d’IA pour améliorer le couplage, la qualité et l’utilisabilité des données, notamment via des systèmes synthétiques innovants tels que les jumeaux statistiques numériques et les cadres de classification multi-agents. La transparence et l’explicabilité sont apparues comme des principes critiques, garantissant que les résultats de l’IA restent interprétables, fiables et conformes aux standards statistiques établis. Par ailleurs, la préparation organisationnelle — incluant l’infrastructure numérique, les compétences spécialisées et un cadre réglementaire approprié — a été mise en avant comme un prérequis indispensable à l’adoption réussie de l’IA. Collectivement, ces avancées promettent de transformer la méthodologie des enquêtes et le traitement des données administratives en fonctions plus agiles, centrées utilisateur et pertinentes pour la politique, renforçant ainsi le rôle vital des statistiques officielles dans un écosystème de données de plus en plus complexe.
