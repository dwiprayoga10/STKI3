#!/usr/bin/env python
# coding: utf-8

# In[1]:


teks = "<p>Ini adalah contoh! teks dengan beberapa tanda baca.</p>"
teks_bersih = ''.join(e for e in teks if e.isalnum() or e.isspace())
print(teks_bersih)



# In[ ]:





# In[2]:


teks = "Ini adalah contoh teks."
tokens = teks.split()
print(tokens)


# In[3]:


from nltk.stem import PorterStemmer

ps = PorterStemmer()
kata = "running"
kata_dasar = ps.stem(kata)
print(kata_dasar)


# In[ ]:




