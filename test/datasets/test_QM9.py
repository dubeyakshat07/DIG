from dig.ggraph.dataset import ggraph_dataset

def test_qm9():
    dataset = ggraph_dataset.QM9(root='./dataset', prop_name='penalized_logp')
    assert len(dataset) == 133885