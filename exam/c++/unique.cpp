#include <string>
#include <unordered_map>
std::string duplicate_encoder(std::string word){
    std::string result = "";
    std::unordered_map<char, int> charcount;

    for(int i = 0; i<word.length(); ++i){
      char islow = std::tolower(word[i]);
      charcount[islow]++;
    }

    for(int i = 0; i<word.length(); ++i){
      char islow = std::tolower(word[i]);
      if(charcount[islow]==1){
        result+="(";
      } 
      else {
        result+=")";
      }
    }  
    return result; 
}