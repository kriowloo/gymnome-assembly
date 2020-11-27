from gym import spaces, Env
import numpy as np

class BaseEnv(Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, reads):
        super(BaseEnv, self).__init__()
        self.reads = reads
        self.n_reads = len(self.reads)
        self.action_space = spaces.Discrete(self.n_reads)
        self.observation_space = spaces.Tuple(tuple([spaces.Discrete(self.n_reads + 1) for _ in range(self.n_reads)]))
        self.overlap_buffer = {}
        self._start()

    def _start(self):
        self.cur_pos = 0
        aux = np.empty(self.n_reads)
        aux.fill(-1)
        self.cur_state = self._to_tuple(aux)

    def _to_tuple(self, array):
        return tuple(int(v) for v in array)

    def _is_terminal(self, obs):
        control = np.zeros(self.n_reads)
        for read_id in obs:
            control[read_id] = 1
        return np.count_nonzero(control) == self.n_reads

    def _is_final(self, obs):
        for o in obs:
            if o == -1:
                return False
        return True

    def _get_sw_matrix(self, i, j, matrix, s1, s2, match, mismatch, gap):
        score = match if s1[i-1] == s2[j-1] else mismatch
        return max(
            matrix[i-1][j-1] + score,
            matrix[i-1][j] + gap,
            matrix[i][j-1] + gap,
            0
        )

    def _get_sw_score(self, s1, s2, match = 1.0, mismatch = -0.33, gap = -1.33):
        l = len(s1)+1
        c = len(s2)+1
        matrix = np.array([0.0 for _ in range(l * c)]).reshape(l, c)
        for i in range(1, l):
            for j in range(1, c):
                matrix[i][j] = self._get_sw_matrix(i, j, matrix, s1, s2, match, mismatch, gap)
        return np.max(matrix)

    def _get_cached_overlap(self, read1, read2):
        if read1 in self.overlap_buffer and read2 in self.overlap_buffer[read1]:
            return self.overlap_buffer[read1][read2]
        if read2 in self.overlap_buffer and read1 in self.overlap_buffer[read2]:
            return self.overlap_buffer[read2][read1]
        return None

    def _cache_overlap(self, read1, read2, value):
        if read1 not in self.overlap_buffer:
            self.overlap_buffer[read1] = {}
        self.overlap_buffer[read1][read2] = value

    def _get_overlap(self, read1, read2):
        o_val = self._get_cached_overlap(read1, read2)
        if o_val is None:
            s1 = self.reads[read1]
            s2 = self.reads[read2]
            o_val = self._get_sw_score(s1, s2)
            self._cache_overlap(read1, read2, o_val)
        return o_val

    def _compute_reward(self, state, done):
        if not done or not self._is_terminal(state):
            return 0.1
        acc = 0.0
        last = None
        for read_id in state:
            if last is not None:
                acc += self._get_overlap(last, read_id)
            last = read_id
        return acc

    def step(self, action):
        # copy current tuple
        next = np.empty(self.n_reads)
        next.fill(-1)
        for i in range(self.cur_pos):
            next[i] = self.cur_state[i]
        # set current action into next state
        next[self.cur_pos] = action
        # set next state as current state
        self.cur_state = self._to_tuple(next)
        self.cur_pos += 1
        obs = self.cur_state
        done = self._is_final(obs)
        reward = self._compute_reward(obs, done)
        info = None
        return obs, reward, done, info

    def reset(self):
        self._start()
        return self.cur_state

    def render(self, mode='human', close=False):
        print(self.cur_state)
        
class Dataset01v1(BaseEnv):
    def __init__(self):
        reads = ['ACCGT', 'CGTGC', 'TTAC', 'TACCGT']
        super().__init__(reads)

class Dataset01v2(BaseEnv):
    def __init__(self):
        reads = ['ACCGT', 'CGTGC', 'TTAC', 'TACCGT']
        super().__init__(reads)