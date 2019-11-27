class Singleton {
public:
   static Singleton* Instance();
private:
   Singleton(){};  // Private so that it can  not be called
   Singleton(Singleton const&){};             // copy constructor is private
   Singleton& operator=(Singleton const&){};  // assignment operator is private
   static Singleton* m_instance;
15
};

