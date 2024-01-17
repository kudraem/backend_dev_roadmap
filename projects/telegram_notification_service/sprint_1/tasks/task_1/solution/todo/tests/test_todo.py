from todo.script import Todo


def test_todo():
    new = Todo()
    response = new.enlist(10)
    assert response[1]['id'] == 2
    response = new.enlist(10, 5)
    assert response[6]['id'] == 12
    response = new.id(5)
    assert response['todo'] == "Solve a Rubik's cube"
    response = new.random()
    assert response['id'] > 0
    response = new.user(5)
    assert response[0]['userId'] == 5
    response = new.add('Send another request to dummyjson.com', 31, False)
    assert response['id'] == 151
    response = new.update(1, False)
    assert response['completed'] is False
    response = new.remove(1)
    assert response['isDeleted'] is True
    print('Tests passed')


test_todo()
