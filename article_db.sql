PGDMP     '    4                z         
   article_db    14.1    14.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24576 
   article_db    DATABASE     n   CREATE DATABASE article_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE article_db;
                postgres    false            �            1259    24581 
   article_tb    TABLE     �   CREATE TABLE public.article_tb (
    article_title character varying(300),
    article_description text,
    article_id integer
);
    DROP TABLE public.article_tb;
       public         heap    postgres    false            �            1259    24577    articles    TABLE     "   CREATE TABLE public.articles (
);
    DROP TABLE public.articles;
       public         heap    postgres    false            �          0    24581 
   article_tb 
   TABLE DATA           T   COPY public.article_tb (article_title, article_description, article_id) FROM stdin;
    public          postgres    false    210   �       �          0    24577    articles 
   TABLE DATA           "   COPY public.articles  FROM stdin;
    public          postgres    false    209          �   W   x����!��9�,3E�В3#3=#�R���(51E!?M!&Wed�KP�,d��RP+�ځ[�t*�4#04	j�]��� �!�K      �      x������ � �     