import requests

def pokemon():
    
    while True:
        poke_name = input("pokemon Name = ")

        if poke_name=="done":
            break
        else:
            try:

                endpoint = "https://pokeapi.co/api/v2/pokemon/"
                response = requests.get(endpoint + poke_name )
                response = response.json()
                print("Weight: ", response['weight'])

            except:
                print("please this is not a pokemon name, try again!!")
                continue

pokemon()
            


# if __name__ == "__main__":
    