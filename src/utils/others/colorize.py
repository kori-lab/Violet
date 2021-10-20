def run (text: str, optionReturn=False) -> tuple[str, None]:
  colorList = {
        ("black"                    , "b"   ,  "preto"              , "p"   ) : "\u001b[30m"  ,
        ("red"                      , "r"   ,  "vermelho"           , "v"   ) : "\u001b[31m"  ,
        ("green"                    , "g"   ,  "verde"              , "vd"  ) : "\u001b[32m"  ,
        ("yellow"                   , "y"   ,  "amarelo"            , "a"   ) : "\u001b[33m"  ,
        ("blue"                     , "bl"  , "azul"                , "az"  ) : "\u001b[34m"  ,
        ("magenta"                  , "m"                                   ) : "\u001b[35m"  ,
        ("cyan"                     , "c"   ,  "ciano"                      ) : "\u001b[36m"  ,
        ("white"                    , "w"   ,  "branco"             , "bn"  ) : "\u001b[37m"  ,
        ("bright black"             , "bb"  , "preto claro"         , "pc"  ) : "\u001b[30;1m",
        ("bright red"               , "br"  , "vermelho claro"      , "rc"  ) : "\u001b[31;1m",
        ("bright green"             , "bg"  , "verde claro"         , "vdc" ) : "\u001b[32;1m",
        ("bright yellow"            , "by"  , "amarelo claro"       , "ac"  ) : "\u001b[33;1m",
        ("bright blue"              , "bb"  , "azul claro"          , "azc" ) : "\u001b[34;1m",
        ("bright magenta"           , "bm"  , "magenta claro"       , "mc"  ) : "\u001b[35;1m",
        ("bright cyan"              , "bc"  , "ciano claro"         , "cc"  ) : "\u001b[36;1m",
        ("bright white"             , "bw"  , "branco claro"        , "bc"  ) : "\u001b[37;1m",
        ("background black"         , "bgb" , "fundo preto"         , "fp"  ) : "\u001b[40m"  ,
        ("background red"           , "bgr" , "fundo vermelho"      , "fv"  ) : "\u001b[41m"  ,
        ("background green"         , "bgg" , "fundo verde"         , "fvd" ) : "\u001b[42m"  ,
        ("background yellow"        , "bgy" , "fundo amarelo"       , "fa"  ) : "\u001b[43m"  ,
        ("background blue"          , "bgb" , "fundo azul"          , "faz" ) : "\u001b[44m"  ,
        ("background magenta"       , "bgm" , "fundo magenta"       , "fm"  ) : "\u001b[45m"  ,
        ("background cyan"          , "bgc" , "fundo ciano"         , "fc"  ) : "\u001b[46m"  ,
        ("background white"         , "bgw" , "fundo branco"        , "fb"  ) : "\u001b[47m"  ,
        ("background bright black"  , "bgbb", "fundo preto claro"   , "fpc" ) : "\u001b[40m"  ,
        ("background bright red"    , "bgbr", "fundo vermelho claro", "fvc" ) : "\u001b[41m"  ,
        ("background bright green"  , "bgbg", "fundo verde claro"   , "fvdc") : "\u001b[42m"  ,
        ("background bright yellow" , "bgby", "fundo amarelo claro" , "fac" ) : "\u001b[43m"  ,
        ("background bright blue"   , "bgbb", "fundo azul claro"    , "fazc") : "\u001b[44m"  ,
        ("background bright magenta", "bgbm", "fundo magenta claro" , "fmc" ) : "\u001b[45m"  ,
        ("background bright cyan"   , "bgbc", "fundo ciano claro"   , "fcc" ) : "\u001b[46m"  ,
        ("background bright white"  , "bgbw", "fundo branco claro"  , "fbc" ) : "\u001b[47m"  ,
        ("bold"                     , "bd"  , "negrito"             , "n"   ) : "\u001b[1m"   ,
        ("underline"                , "un"  , "sublinhado"          , "s"   ) : "\u001b[4m"   ,
        ("reversed"                 , "rv"  , "revertido"                   ) : "\u001b[7m"   ,
        ("::"                                                               ) : "\u001b[0m"
    };
  
  formatString = text;

  for cores in colorList.keys():
      if cores == "::": 
        formatString = formatString.replace(f"{cores}", colorList[cores]) + colorList["::"];

      else:
        for cor in cores:
        	formatString = formatString.replace(f":{cor}:", colorList[cores]);
  
  if optionReturn:
    return print(formatString);
  
  return formatString;