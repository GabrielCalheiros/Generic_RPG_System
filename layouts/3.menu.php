<?php



function print_menu_card($nome,$links){
    echo'
    <a href="./'.$links.'">
    <div class="cardBiblioteca">
    <div class="texto">
    <h1>'.$nome.'</h1></div>
    <div class="seta-direita"><img src="./images/seta.svg" class="seta_some"></div>
    <div class="seta-esquerda"><img src="./images/seta.svg" class="seta_some
            seta_virada"></div>
    </div></a>
    ';
}

function listMenu(array $nomes): array{
    echo'
    <style>
	.cardBiblioteca {
  display: grid;
  grid-template-columns: 30% 40% 30%;
  grid-template-rows: 100%;
  gap: 5px 8px;
  /*grid-auto-flow: row;*/
  grid-template-areas:
    "seta-esquerda texto seta-direita";
  width: 100%;
  height: 10%;
  margin-left: auto;
  margin-right: auto;
  max-width: 500px;
}

.cardBiblioteca:hover .seta_some, .cardBiblioteca:hover .seta-esquerda, .cardBiblioteca:hover .seta-direita {
    display: block;
    filter: invert(0%);
  }

  .cardBiblioteca:hover h1 {
    color: goldenrod;
  }

  .texto {
    grid-area: texto;
    text-align: center;
    align-self: center;
    text-decoration: none;

  }


.seta-direita {
    grid-area: seta-direita;
    align-self: center;
    text-align: -webkit-right;
    filter: invert(100%);
    transition: 0.5s;
  }
  
  .seta-esquerda {
    grid-area: seta-esquerda;
    align-self: center;
    text-align: -webkit-left;
    filter: invert(100%);
    transition: 0.5s;
  }

  .seta_some {
    display: none;
    width: 100%;
  }

  .seta_virada {
    transform: rotate(180deg);
    width: 100%;
  }
  

</style>
';
    foreach($nomes as $items => $links){
        print_menu_card($item,$link);
    }
    return nomes;
}



?>
