% -------------------------------
% SISTEMA DE RIEGO MEJORADO
% -------------------------------

% ========== BASE DE CONOCIMIENTO ==========
% Hechos dinámicos para permitir modificaciones en tiempo real
:- dynamic humedad_suelo/1, temperatura/1, hora/1, pronostico_lluvia/1.

% Datos iniciales (pueden cambiarse con assert/retract)
humedad_suelo(baja).
temperatura(35).
hora(20).
pronostico_lluvia(false).

% ========== REGLAS MEJORADAS ==========
% Hora adecuada para riego (con validación)
hora_adecuada :-
    hora(H),
    number(H),      % Verifica que sea un número
    between(0,23,H), % Hora válida (0-23)
    (H < 10 ; H > 18).

% Regla principal mejorada con validaciones
activar_riego :-
    humedad_suelo(baja),
    pronostico_lluvia(false),
    hora_adecuada,
    \+ alerta_calor. % No activar si hay alerta de calor

% Sistema de alertas mejorado
alerta_calor :-
    temperatura(T),
    number(T),
    T >= 32. % Temperatura peligrosa

alerta_sequia :-
    humedad_suelo(muy_baja),
    temperatura(T), T > 30.

% ========== SISTEMA DE RECOMENDACIONES ==========
recomendacion :-
    activar_riego,
    alerta_calor, !,
    writeln('ALERTA: Temperatura peligrosa detectada'),
    writeln('RECOMENDACION: Postergue riego o use sistema por goteo nocturno').

recomendacion :-
    alerta_sequia, !,
    writeln('ALERTA CRITICA: Sequia extrema detectada'),
    writeln('RECOMENDACION: Riego de emergencia inmediato').

recomendacion :-
    activar_riego, !,
    writeln('RIEGO AUTORIZADO: Condiciones óptimas detectadas').

recomendacion :-
    writeln('SISTEMA EN ESPERA: No se requieren acciones').

% ========== INTERFAZ DE DIAGNÓSTICO ==========
estado_riego('SISTEMA ACTIVADO') :- activar_riego.
estado_riego('SISTEMA EN ESPERA') :- \+ activar_riego.

% ========== HELPERS PARA PRUEBAS ==========
% Predicado para mostrar todos los sensores
estado_sensores :-
    writeln('\n=== ESTADO ACTUAL DE SENSORES ==='),
    (humedad_suelo(H) -> format('Humedad suelo: ~w~n', [H]) ; writeln('Humedad: No definida')),
    (temperatura(T) -> format('Temperatura: ~w°C~n', [T]) ; writeln('Temperatura: No definida')),
    (hora(H) -> format('Hora actual: ~w:00~n', [H]) ; writeln('Hora: No definida')),
    (pronostico_lluvia(L) -> 
        (L == true -> writeln('Pronostico: Lluvia esperada') ; writeln('Pronostico: No hay lluvia'))
     ; writeln('Pronostico: No definido')),
    writeln('==============================\n').