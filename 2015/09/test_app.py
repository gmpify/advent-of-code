from app import City, Path, find_paths, load_graph, get_shortest_path

def test_add_connection():
    london = City('London')
    dublin = City('Dublin')

    dublin.add_connection(london, 464)
    london.add_connection(dublin, 464)

    assert len(dublin.connections) == 1
    assert len(london.connections) == 1

    assert dublin.connections[london] == 464
    assert london.connections[dublin] == 464


def test_path_add_city():
    london = City('London')
    dublin = City('Dublin')

    dublin.add_connection(london, 464)
    london.add_connection(dublin, 464)

    path = Path(london)
    path.add_city(dublin)

    path.total_distance == 464


def test_load_graph():
    result = load_graph('test.txt')

    assert len(result) == 3

    assert City('London').name == result['London'].name
    assert City('Dublin').name == result['Dublin'].name
    assert City('Belfast').name == result['Belfast'].name


def test_find_paths():
    graph = load_graph('test.txt')
    result = find_paths(graph)

    assert len(result) == 6


def test_get_shortest_path():
    graph = load_graph('test.txt')
    paths = find_paths(graph)
    result = get_shortest_path(paths)

    assert result.total_distance == 605
