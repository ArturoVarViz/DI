cabecera
========

Para escribir párrafos, solo tenemos que escribir sin marcador. Si queremos remarcar en *cursiva*, la **negrita** entre doble asterisco. Para ejemplos de código en doble comillas ``import sys``.

* El contenido no puede comenzar con un espacio en blanco
* No puede estar añadido
* Tiene que estar separado por caracteres separadores

.. _nivelseccion:

Niveles de sección
^^^^^^^^^^^^^^^^^^

Las diferentes niveles de sección se escriben:

* = para sección
* '-' para subsección (sin comillas)
* ^ para subsección
* `` para párrafos

Listas
^^^^^^

Lista con se marcan con *

Listas desordenadas
-------------------


* lista simple

Listas ordenadas
^^^^^^^^^^^^^^^^

1. Primer Elemento
2. Elemento
   2.1. Con subniveles
   2.2. También de forma muy sencilla

#. Otro tipo de lista
#. Ordenada

Lista de definiciones
^^^^^^^^^^^^^^^^^^^^^

Término (primera línea de texto)
    Definición de término, que tienes que estar tabulado

    Puedes tener varias líneas o varios párrafos
Término dos
    Con esto puedes hacer varios

Bloque Literario
^^^^^^^^^^^^^^^^

Después de un texto normal, puedes dejar un párrafo con un ejemplo de código::

    def funcion(valor):

        var = valor
        print(var)

El texto normal continúa después del bloque

Bloque Doctest
^^^^^^^^^^^^^^

Para los bloques de Doctest no requieres ninguna

>>> 1+1
2

Hipervínculo
^^^^^^^^^^^^

enlaces

``Enlace externo``


Podemos consultar la documentación de uso de `restructuredtext <http://www.sphinx.doc.org/en(master/userge/restruturedtext/basics.html>`_

El párrafo tiene un enlace a la página de centro `Daniel Castelao`_

.. _Daniel Castelao: https://www.danielcastelao.org

``Enlaces internos``


Puedes hacer una referencia con una etiqueta colocada
:ref:`_nivelesseccion`
