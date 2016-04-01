/* selecionando a media geral de bikes disponiveis de uma estacao por horas do dia */
select e.idEstacao as 'Numero da Estacao' , e.nome  as 'Nome',  AVG(vagasOcupadas) as 'Media de Bikes Disponiveis', strftime('%H', m.timestamp) as 'Horario'
	from movimentacao m, estacao e 
	where e.idEstacao = m.idEstacao and m.idEstacao = 114
	group by strftime('%H', m.timestamp) ;

/* selecionando a media geral de bikes disponiveis de uma estacao por horas do dia apenas para quintas feiras. Cuidado que strftime retorna string */
select e.idEstacao as 'Numero da Estacao' , e.nome  as 'Nome', AVG(vagasOcupadas) as 'Media de Bikes Disponiveis', strftime('%H', m.timestamp) as 'Horario' , strftime('%w', m.timestamp) as 'Dia da Semana'
	from movimentacao m, estacao e 
	where e.idEstacao = m.idEstacao and m.idEstacao = 114  and strftime('%w', m.timestamp) = '4'
	group by strftime('%H', m.timestamp) ; 

/* ver as últimas inserções */	
select * from movimentacao order by id DESC