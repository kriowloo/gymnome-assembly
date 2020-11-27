# OpenAI Gym Environments: gymnome-assembly

## Description:

Each environment describes a set of reads to be assembled by the agent. All these reads were generated using sequencing simulation without sequencing errors and they can be seen through attribute reads of each environment (eg.: env.reads). Similarly, the microgenome used to generated them also can be accessed  through the attribute microgenome of each environment (eg.: env.microgenome). Finally, an optimal permutation of reads can be obtained through the method getOptimalPermutation (eg.: env.getOptimalPermutation()).

## Observation:

Type: *Box( number of reads )*
		
Each state is an array that represents a permutation of reads. Each array element contains a read index (starting from 0)  or -1 when no read was chosen (eg.: initial state is entirely filled with -1).

## Actions:

Type: *Discrete( number of reads )*

Each action corresponds to a read index (starting from 0).

## Reward:

Rewards depends on the version you decide to use.	In version **v1**, reward is 0.1 for every step that leads to a non-terminal state; otherwise it corresponds to an overlap score (calculated by SmithWaterman algorithm). In version **v2**, reward is 0.1 for every step taken from initial state; otherwise it corresponds to a normalized overlap score (from 0 to 1). If the action leads to a terminal state, the reward is added by 1.

## Starting State:

A unique state totally filled with -1.

## Episode Termination:

Episodes terminate when an absorbing state is reached.

## List of environments:

Genome size | Number of reads | Read length | Env. name (v1) | Env. name (v2)
------------ | ------------- | ------------- | ------------- | -------------
25 | 10 | 8 | GymnomeAssembly_25_10_8-v1 | GymnomeAssembly_25_10_8-v2
25 | 10 | 10 | GymnomeAssembly_25_10_10-v1 | GymnomeAssembly_25_10_10-v2
25 | 10 | 15 | GymnomeAssembly_25_10_15-v1 | GymnomeAssembly_25_10_15-v2
25 | 20 | 8 | GymnomeAssembly_25_20_8-v1 | GymnomeAssembly_25_20_8-v2
25 | 20 | 10 | GymnomeAssembly_25_20_10-v1 | GymnomeAssembly_25_20_10-v2
25 | 20 | 15 | GymnomeAssembly_25_20_15-v1 | GymnomeAssembly_25_20_15-v2
25 | 30 | 8 | GymnomeAssembly_25_30_8-v1 | GymnomeAssembly_25_30_8-v2
25 | 30 | 10 | GymnomeAssembly_25_30_10-v1 | GymnomeAssembly_25_30_10-v2
25 | 30 | 15 | GymnomeAssembly_25_30_15-v1 | GymnomeAssembly_25_30_15-v2
50 | 10 | 8 | GymnomeAssembly_50_10_8-v1 | GymnomeAssembly_50_10_8-v2
50 | 10 | 10 | GymnomeAssembly_50_10_10-v1 | GymnomeAssembly_50_10_10-v2
50 | 10 | 15 | GymnomeAssembly_50_10_15-v1 | GymnomeAssembly_50_10_15-v2
50 | 20 | 8 | GymnomeAssembly_50_20_8-v1 | GymnomeAssembly_50_20_8-v2
50 | 20 | 10 | GymnomeAssembly_50_20_10-v1 | GymnomeAssembly_50_20_10-v2
50 | 20 | 15 | GymnomeAssembly_50_20_15-v1 | GymnomeAssembly_50_20_15-v2
50 | 30 | 8 | GymnomeAssembly_50_30_8-v1 | GymnomeAssembly_50_30_8-v2
50 | 30 | 10 | GymnomeAssembly_50_30_10-v1 | GymnomeAssembly_50_30_10-v2
50 | 30 | 15 | GymnomeAssembly_50_30_15-v1 | GymnomeAssembly_50_30_15-v2
381 | 20 | 75| GymnomeAssembly_381_20_75-v1 | GymnomeAssembly_381_20_75-v2
567 | 30 | 75| GymnomeAssembly_567_30_75-v1 | GymnomeAssembly_567_30_75-v2
726 | 40 | 75| GymnomeAssembly_726_40_75-v1 | GymnomeAssembly_726_40_75-v2
930 | 50 | 75| GymnomeAssembly_930_50_75-v1 | GymnomeAssembly_930_50_75-v2
4224 | 230 | 75| GymnomeAssembly_4224_230_75-v1 | GymnomeAssembly_4224_230_75-v2
