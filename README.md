# RipBikeSampa
Uma simples maneira de coletar os dados das estações do BikeSampa e mostrar para eles que há sim desfalque de bikes em certas estações.  
Código simples e sucinto. Existem outros serviços que fornecem esse mesmo tipo de informação e entregam o mesmo tipo de dado, mas quando me interessei em monitorar as estações que utilizo do BikeSampa não conhecia nenhum desses serviços, alias, procurar por eles no Google não é uma tarefa tão simples, cheguei até eles por indicação de um professor da faculdade.

Serviços alternativos para coleta de dados:  
http://citybik.es/  
http://api.citybik.es/  
http://api.citybik.es/bikesampa.json  
http://api.citybik.es/v2/networks/bikesampa  


É necessário adicionar o SQLAlchemy nas bibliotecas python do seu sistema.
Tente: pip install sqlalchemy  

De permissões de acesso para a pasta.  

Adicione a execução do servico.py ao cron do seu Linux, digite: "crontab -e"  
Adicione essas linhas no arquivo:
"* 6-21 * * * python (caminho_do_projeto)/servico.py" 
"1 22 * * * python (caminho_do_projeto)/servico.py"
assim ele executará minuto a minuto das 6h as 21:59h e 1x as 22h todos os dias.
