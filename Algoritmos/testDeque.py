from implementacao.Queue import Deque as Queue


deque = Queue(5)

deque.insere_inicio(3)
deque.insere_final(5)
deque.insere_final(10)
deque.insere_inicio(2)
deque.insere_final(11)

deque.insere_inicio(43)
deque.excluir_inicio()
deque.exclui_final()
deque.get_inicio()
deque.get_final()
