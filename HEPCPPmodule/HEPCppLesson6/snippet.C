{
  float x = 5.;
  float y = 2.;
  float res = TMath::Power(x,2.) - y*TMath::Exp(-x);
  std::cout << res << std::endl;
}
