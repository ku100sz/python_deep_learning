{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMoHcm7mM2tHfSATywtmA+B",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ku100sz/python_deep_learning/blob/t5/checktriangle.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "QsS4V9pD8YU0"
      },
      "outputs": [],
      "source": [
        "def checktriangle(a,b,c):\n",
        "  check=0\n",
        "  if a<b+c:\n",
        "    if b<a+c:\n",
        "      if c<a+b:\n",
        "        check=1\n",
        "  if check==1:\n",
        "    return \"true\"\n",
        "  else:\n",
        "    return \"false\""
      ]
    }
  ]
}