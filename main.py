from pyscript import document 

def candidate_checker(e): 
    club_members = ['anthea alavado', 'aria bonsol', 'gabi ibarra', 'cai torrejon', 'jillianne singh', 'yoninah lim', 'jadenne saquido', 'lexi joaquin', 'yijin jeong', 'shimeia sanchez']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f'{f_name.strip()} {l_name.strip()}'
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.', 
                f'Congratulations,{candidate}! You are now part of the Luminara Dance Club!') 

document.getElementById('result').innerHTML=messages[member_checker]
