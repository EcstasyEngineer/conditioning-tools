from .base import Cycler
from typing import List, Dict

class ClusterCycler(Cycler):
    """
    Treats lines in small groups (clusters).
    For simplicity, cluster_size=3 means we group lines in triples and cycle.
    """
    def __init__(self, lines: List[Dict], cluster_size: int = 3):
        super().__init__(lines)
        self.cluster_size = cluster_size

    def get_sequence(self) -> List[Dict]:
        # Group into clusters:
        clusters = [self.lines[i:i+self.cluster_size] for i in range(0, len(self.lines), self.cluster_size)]
        # Just return them in order for now:
        result = []
        for cluster in clusters:
            result.extend(cluster)
        return result
