import pickle
import keyboard   
# Defining a dictionary that stores muscle names to recommended exercises and steps
muscle_dict = {
    "biceps" : [
        {"name": "Dumbbell curls", "steps": ["1. Stand with your feet shoulder-width apart and your arms extended at your sides holding a dumbbell in each hand.", "2. Curl the weights up towards your shoulders, keeping your elbows close to your sides.", "3. Lower the weights back down to your sides."]},
        {"name": "Barbell curls", "steps": ["1. Stand with your feet shoulder-width apart and your arms extended at your sides holding a barbell with an underhand grip.", "2. Curl the bar up towards your shoulders, keeping your elbows close to your sides.", "3. Lower the bar back down to your sides."]},
        {"name": "Hammer curls", "steps": ["1. Stand with your feet shoulder-width apart and your arms extended at your sides holding a dumbbell in each hand with a neutral grip.", "2. Curl the weights up towards your shoulders, keeping your elbows close to your sides.", "3. Lower the weights back down to your sides."]},
        {"name": "Chin-ups", "steps": ["1. Grab a pull-up bar with your palms facing towards you and your hands shoulder-width apart.", "2. Pull yourself up until your chin is above the bar.", "3. Lower yourself back down."]},
        {"name": "Preacher curls", "steps": ["1. Sit on a preacher bench with your arms extended over the pad and your palms facing up.", "2. Curl the weight up towards your shoulders, then lower it back down."]},
        {"name": "Concentration curls", "steps": ["1. Sit on a bench with your legs spread apart and your elbow resting on your inner thigh.", "2. Curl the weight up towards your shoulder, then lower it back down."]}
        ],
        "triceps": [
            {"name": "Tricep extensions", "steps": ["1. Stand with your feet shoulder-width apart and your arms extended overhead holding a dumbbell with both hands.", "2. Lower the weight behind your head, keeping your elbows close to your head.", "3. Raise the weight back up to the starting position."]},
            {"name": "Close-grip bench press", "steps": ["1. Lie on a bench with your hands shoulder-width apart and your palms facing away from you.", "2. Lower the bar towards your chest, keeping your elbows close to your sides.", "3. Push the bar back up to the starting position."]},
            {"name": "Dips", "steps": ["1. Stand between two parallel bars and grip them with your palms facing down.", "2. Lower your body until your arms form a 90-degree angle.", "3. Push yourself back up to the starting position."]},
            {"name": "Skull crushers", "steps": ["1. Lie on a bench with your arms extended over your head and your palms facing up.", "2. Lower the weight towards your forehead, keeping your elbows close to your head.", "3. Raise the weight back up to the starting position."]},
            {"name": "Close-grip push-ups", "steps": ["1. Get into a push-up position with your hands close together.", "2. Lower your body until your chest almost touches the ground.", "3. Push yourself back up to the starting position."]}
        ],
    "chest": [
            {"name": "Bench press", "steps": ["1. Lie on a bench with your feet flat on the ground and your hands shoulder-width apart holding a barbell.", "2. Lower the bar towards your chest, keeping your elbows close to your sides.", "3. Push the bar back up to the starting position."]},
            {"name": "Push-ups", "steps": ["1. Get into a plank position with your hands shoulder-width apart.", "2. Lower your body until your chest almost touches the ground.", "3. Push yourself back up to the starting position."]},
            {"name": "Chest flys", "steps": ["1. Lie on a bench with your arms extended over your chest and your palms facing each other holding a dumbbell in each hand.", "2. Lower the weights out to the sides, keeping your elbows slightly bent.", "3. Bring the weights back up to the starting position."]},
            {"name": "Incline bench press", "steps": ["1. Lie on an incline bench with your feet flat on the ground and your hands shoulder-width apart holding a barbell.", "2. Lower the bar towards your chest, keeping your elbows close to your sides.", "3. Push the bar back up to the starting position."]},
            {"name": "Dumbbell flys", "steps": ["1. Lie on a flat bench with your feet flat on the floor.", "2. Hold a dumbbell in each hand with your arms extended above your chest.", "3. Lower the dumbbells out to the sides, then bring them back up to the starting position."]},
            {"name": "Decline Bench", "steps": ["1. Lie on a decline bench with your feet secured at the end of the bench.", "2. Grasp the barbell with your hands slightly wider than shoulder-width apart.", "3. Lower the barbell to your chest, then push it back up to the starting position."]}
        ],
    "back": [
            {"name": "Deadlift", "steps": ["1. Stand with your feet shoulder-width apart and your toes pointing forward.", "2. Grasp the barbell with your hands shoulder-width apart.", "3. Lift the barbell off the ground by extending your legs and hips."]},
            {"name": "Pull-ups", "steps": ["1. Grab the pull-up bar with your palms facing away from you and your hands shoulder-width apart.", "2. Hang from the bar with your arms fully extended.", "3. Pull yourself up until your chin is above the bar, then lower yourself back down to the starting position."]},
            {"name": "Lat pulldowns", "steps": ["1. Sit at a lat pulldown machine with your feet flat on the ground.", "2. Grasp the bar with your hands slightly wider than shoulder-width apart.", "3. Pull the bar down towards your chest, then slowly release it back up to the starting position."]},
            {"name": "Seated cable rows", "steps": ["1. Sit at a cable row machine with your feet flat on the ground.", "2. Grasp the cable handles with your hands.", "3. Pull the cable towards your chest, then slowly release it back up to the starting position."]}

        ],
    "legs": [
            {"name": "Squats", "steps": ["1.Stand with your feet shoulder-width apart and your toes pointing forward.", "2. Grasp the barbell with your hands slightly wider than shoulder-width apart.", "3. Lower your body down by bending your knees, then push yourself back up to the starting position."]},
            {"name": "Lunges", "steps": ["1.Stand with your feet shoulder-width apart.", "2. Take a step forward with one foot, then lower your body down by bending your knees.", "3. Push yourself back up to the starting position, then repeat with the other foot."]},
            {"name": "Leg press", "steps": ["1. Sit at a leg press machine with your feet flat on the platform.", "2. Grasp the handles with your hands.", "3.Push the platform away from your body, then slowly release it back towards your body."]},
            {"name": "Calf raises", "steps": ["1.Stand with your feet shoulder-width apart.", "2. Raise your heels off the ground, then slowly lower them back down.", "3. Repeat for the desired number of repetitions."]},
            {"name": "Leg curls", "steps": ["1. Lie face down on a leg curl machine with your feet hooked under the padded bar.", "2. Grasp the cable handles with your hands.", "3.Curl your legs up towards your buttocks, then slowly release them back down to the starting position."]}
        ],}


with open("muscle_dict.pkl", "wb") as f:
    pickle.dump(muscle_dict, f)

with open("muscle_dict.pkl", "rb") as f:
    muscle_dict = pickle.load(f)

while True:
    try:
    
        if keyboard.is_pressed("enter"):
            muscle_name = input("Enter a muscle name: ")
            if muscle_name in muscle_dict:
                print("Recommended exercises for", muscle_name, "are:")
                for exercise in muscle_dict[muscle_name]:
                    print(exercise["name"])
                    print("Steps:")
                    for step in exercise["steps"]:
                        print("- " + step)
                    print("\n")
                print("For detailed instructions on how to perform these exercises, please refer to https://musclewiki.com")
            else:
                print("Muscle name not found in dictionary.\n Try to enter the muscle name in lower case\n Supported muscles are - \n chest, \n back, \n legs, \n biceps")
    except:

        break