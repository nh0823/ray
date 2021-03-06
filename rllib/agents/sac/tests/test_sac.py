import unittest

import ray
import ray.rllib.agents.sac as sac
from ray.rllib.utils.framework import try_import_tf
from ray.rllib.utils.test_utils import framework_iterator

tf = try_import_tf()


class TestSAC(unittest.TestCase):
    def test_sac_compilation(self):
        """Test whether an SACTrainer can be built with all frameworks."""
        ray.init()
        config = sac.DEFAULT_CONFIG.copy()
        config["num_workers"] = 0  # Run locally.
        num_iterations = 1

        # eager (discrete and cont. actions).
        for _ in framework_iterator(config, ["tf", "eager"]):
            for env in [
                    "CartPole-v0",
                    "Pendulum-v0",
            ]:
                print("Env={}".format(env))
                trainer = sac.SACTrainer(config=config, env=env)
                for i in range(num_iterations):
                    results = trainer.train()
                    print(results)


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(["-v", __file__]))
