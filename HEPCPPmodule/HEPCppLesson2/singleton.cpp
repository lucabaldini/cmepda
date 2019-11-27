
Singleton* Singleton::m_instance = NULL;

Singleton* Singleton::instance(){
 if(!m_instance) m_instance=new Singleton();
 return m_instance;
}
