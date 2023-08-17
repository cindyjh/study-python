{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "653f5339",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[90, 88, 75, 80]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores = [70, 75, 80, 65, 88, 90]\n",
    "[scores[len(scores) - 1], scores[-2]] + scores[1:3] # 마이너스 인덱스 사용 가능"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4429c691",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruit_list = ['apple', 'banana', 'orange']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7aba65d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['banana', 'orange']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bf428700",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'banana', 'orange']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "75b2de96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['banana', 'orange']"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list[1:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fb91f6df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'banana', 'orange']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list[:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b81c2588",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'kiwi', 'orange']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list[1] = 'kiwi'\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a51c73fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'strawberry', 'blueberry']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list[1:3] = ['strawberry', 'blueberry']\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "64a7a538",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'strawberry', 'mango', 'blueberry']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list.insert(2, 'mango') # insert\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "24f09af3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'strawberry', 'mango', 'blueberry', 'waterelon']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list.append('waterelon') # append\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cae33ab8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple',\n",
       " 'strawberry',\n",
       " 'mango',\n",
       " 'blueberry',\n",
       " 'waterelon',\n",
       " 'carrot',\n",
       " 'tomato',\n",
       " 'onion']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vegetable_list = ['carrot', 'tomato', 'onion'] \n",
    "fruit_list.extend(vegetable_list) # extend\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "71c91c58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, '가', '나', '다']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1, list2 = [1,2,3], ['가', '나', '다']\n",
    "list3 = list1 + list2\n",
    "list3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2f9ecac8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['strawberry', 'mango', 'blueberry', 'waterelon', 'carrot', 'tomato', 'onion']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list.remove('apple')\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "410fea17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['strawberry', 'mango', 'blueberry', 'waterelon', 'carrot', 'tomato']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del fruit_list[-1]\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "bb6d4a49",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'fruit_list' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[21], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m fruit_list\n\u001b[1;32m----> 2\u001b[0m fruit_list\n",
      "\u001b[1;31mNameError\u001b[0m: name 'fruit_list' is not defined"
     ]
    }
   ],
   "source": [
    "del fruit_list\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "31e7c4b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list = ['apple', 'banana', 'orange']\n",
    "fruit_list.clear()\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "27c0a525",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'blueberry', 'mango', 'strawberry', 'waterelon']"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list = ['apple', 'strawberry', 'mango', 'blueberry', 'waterelon']\n",
    "fruit_list.sort()\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ddb52a8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['waterelon', 'strawberry', 'mango', 'blueberry', 'apple']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_list.sort(reverse=True)\n",
    "fruit_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c2645ab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
