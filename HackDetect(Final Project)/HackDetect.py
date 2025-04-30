# hackdetect.py
import random
import time
import os
import sys
from typing import List, Dict
from dataclasses import dataclass, field
import hashlib
from colorama import init, Fore, Back, Style

@dataclass
class Player:
    name: str
    is_hacker: bool = False
    is_ai: bool = False
    clues_found: List[str] = None
    corrupted_clues: List[str] = None
    can_investigate: bool = True
    active_programs: Dict[str, int] = None

    def __post_init__(self):
        self.clues_found = []
        self.corrupted_clues = []
        self.active_programs = {}
        self.honeypot_data = None
        self.forced_investigation = None
        self.ghost_mode = False
        self.blocked_rounds_remaining = 0
        self.can_investigate = True

@dataclass
class ClueSystem:
    locations: List[str] = field(default_factory=lambda: [
        "Server Room", "Development Network", "Cloud Storage", "Employee Workstations",
        "Security Systems", "Database Cluster", "Backup Systems", "Email Servers",
        "Network Gateway", "Authentication Servers", "Log Archives", "Admin Console"
    ])
    
    attack_patterns: Dict[str, List[str]] = field(default_factory=lambda: {
        "data_theft": [
            "Large data transfer detected to {ip_address} at {timestamp}",
            "Unusual access pattern in {location} - multiple files downloaded",
            "Encrypted tunnel established from {location} to external endpoint",
            "Sensitive data accessed in {location} using {username}'s credentials",
            "Multiple download requests from {location} to unknown endpoint",
            "Data exfiltration attempt detected from {location}",
            "Suspicious file access in {location} at {timestamp}",
            "Unauthorized data transfer from {location} by {username}"
        ],
        "system_breach": [
            "Multiple failed SSH attempts from {ip_address} targeting {location}",
            "Unauthorized elevation of privileges detected in {location}",
            "New backdoor process detected running as {username}",
            "Suspicious service started in {location} with root privileges",
            "Authentication bypass attempt detected at {location}",
            "Unusual sudo activity from {username} in {location}",
            "Suspicious process spawned in {location} at {timestamp}",
            "Unauthorized access attempt to {location} from internal network"
        ],
        "insider_activity": [
            "User {username} accessed sensitive files outside normal hours",
            "Unusual login pattern detected for {username} across multiple systems",
            "Configuration changes made by {username} in {location}",
            "Access granted to {username} for restricted area: {location}",
            "User {username} modified system policies in {location}",
            "Abnormal activity pattern for {username} detected",
            "Multiple failed access attempts by {username} in {location}",
            "Suspicious credential usage by {username} at {timestamp}"
        ],
        "system_manipulation": [
            "System logs deleted in {location} at {timestamp}",
            "Critical service modifications detected in {location}",
            "Suspicious process injection detected in {location}",
            "Configuration file tampering detected in {location}",
            "Unauthorized registry modifications in {location}",
            "System file integrity violation in {location}",
            "Suspicious service configuration change in {location}",
            "Critical system modification by {username} detected"
        ],
        "network_anomaly": [
            "Unusual port scan detected from {location}",
            "Suspicious traffic pattern between {location} and {ip_address}",
            "Network segmentation breach detected at {location}",
            "Anomalous protocol usage detected in {location}",
            "Unexpected outbound connection from {location}",
            "Unusual network behavior in {location} at {timestamp}",
            "Suspicious DNS queries from {location}",
            "Network policy violation detected in {location}"
        ]
    })

    def generate_ip(self) -> str:
        return f"{random.randint(10,254)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

    def generate_timestamp(self) -> str:
        hour = random.randint(0,23)
        minute = random.randint(0,59)
        second = random.randint(0,59)
        return f"{hour:02d}:{minute:02d}:{second:02d}"

    def generate_clues_for_player(self, hacker_name: str, player_seed: str) -> List[str]:
        """Generate unique clues based on both hacker identity and individual player"""
        # Create a unique seed combining hacker name and player seed
        combined_seed = hashlib.md5((hacker_name + player_seed).encode()).hexdigest()
        random.seed(combined_seed)
        
        # Select attack focus for this player
        primary_attack_type = random.choice(list(self.attack_patterns.keys()))
        secondary_attack_type = random.choice(list(self.attack_patterns.keys()))
        
        # Generate consistent IPs and locations for the hacker
        hacker_ip = self.generate_ip()
        hacker_location = random.choice(self.locations)
        
        clues = []
        
        # Generate primary attack clues (more relevant)
        for _ in range(3):  # 3 clues about primary attack
            pattern = random.choice(self.attack_patterns[primary_attack_type])
            clue = pattern.format(
                ip_address=hacker_ip,
                location=hacker_location,
                username=hacker_name,
                timestamp=self.generate_timestamp()
            )
            clues.append(clue)
        
        # Generate some secondary attack clues (less relevant)
        for _ in range(2):  # 2 clues about secondary attack
            pattern = random.choice(self.attack_patterns[secondary_attack_type])
            clue = pattern.format(
                ip_address=self.generate_ip(),
                location=random.choice(self.locations),
                username=random.choice([hacker_name, "admin", "system", "backup", "security"]),
                timestamp=self.generate_timestamp()
            )
            clues.append(clue)
        
        # Add some red herrings (false leads)
        for _ in range(2):
            attack_type = random.choice(list(self.attack_patterns.keys()))
            pattern = random.choice(self.attack_patterns[attack_type])
            clue = pattern.format(
                ip_address=self.generate_ip(),
                location=random.choice(self.locations),
                username=random.choice(["admin", "system", "backup", "security"]),
                timestamp=self.generate_timestamp()
            )
            clues.append(clue)
        
        random.shuffle(clues)
        return clues

class EnhancedUI:
    def __init__(self):
        init()  # Initialize colorama
        self.matrix_chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
        
    def print_glitch_effect(self, text: str, glitch_chance: float = 0.1):
        glitch_chars = "!@#$%^&*()<>{}[]"
        for char in text:
            if random.random() < glitch_chance:
                print(Fore.RED + random.choice(glitch_chars) + Style.RESET_ALL, end='', flush=True)
                time.sleep(0.01)
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()

    def create_progress_bar(self, progress: float, width: int = 40) -> str:
        filled = int(width * progress)
        bar = (Fore.GREEN + '█' * filled + 
               Fore.RED + '░' * (width - filled) + 
               Style.RESET_ALL)
        percentage = f"{progress * 100:.1f}%"
        return f"[{bar}] {percentage}"

    def print_alert_box(self, message: str, alert_type: str = "info"):
        colors = {
            "info": Fore.BLUE,
            "warning": Fore.YELLOW,
            "error": Fore.RED,
            "success": Fore.GREEN
        }
        color = colors.get(alert_type, Fore.WHITE)
        
        width = len(message) + 4
        print(f"{color}╔{'═' * width}╗")
        print(f"║  {message}  ║")
        print(f"╚{'═' * width}╝{Style.RESET_ALL}")

    def matrix_rain(self, duration: float = 1.0):
        """Creates a denser matrix rain effect"""
        try:
            width = os.get_terminal_size().columns
            height = 3  # Limit to 3 lines
            
            start_time = time.time()
            while time.time() - start_time < duration:
                for _ in range(height):
                    # Remove spacing between characters for denser effect
                    rain = ''.join(random.choice(self.matrix_chars) for _ in range(width))
                    print(Fore.GREEN + rain[:width] + Style.RESET_ALL)
                    time.sleep(0.05)
                
                # Move cursor back up
                print(f"\033[{height}A", end='')
            
            # Clear the matrix effect
            print("\n" * height)
            
        except Exception as e:
            print(Fore.GREEN + "システム起動中..." + Style.RESET_ALL)
            time.sleep(duration)

    def create_menu(self, title: str, options: List[str]) -> int:
        """Create an interactive menu with colored options"""
        print(f"\n{Fore.CYAN}{title}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'═' * len(title)}{Style.RESET_ALL}")
        
        for i, option in enumerate(options, 1):
            print(f"{Fore.YELLOW}{i}{Style.RESET_ALL}. {option}")
            
        while True:
            try:
                choice = input(f"\n{Fore.GREEN}Enter your choice >{Style.RESET_ALL} ")
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    return choice_num
                else:
                    self.print_alert_box("Please enter a valid option number", "warning")
            except ValueError:
                self.print_alert_box("Please enter a number", "error")

class HackerGame:
    def __init__(self, num_players: int, include_external_hacker: bool = True):
        self.num_players = num_players
        self.players: List[Player] = []
        self.current_round = 1
        self.max_rounds = 10
        self.game_over = False
        self.hacker_won = False
        self.include_external_hacker = include_external_hacker
        self.terminal_width = os.get_terminal_size().columns
        self.ui = EnhancedUI()  # Initialize the enhanced UI
        self.clue_system = ClueSystem()  # Initialize the clue system
        self.planted_evidence = []  # Initialize planted evidence list
        self.blocked_sharing = set()  # Add this to track blocked sharing pairs
        self.honeypot_targets = {}  # Add this to track honeypot effects


        
        self.logo = Fore.CYAN + """
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██████╗ ███████╗████████╗███████╗ ██████╗████████╗
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
    ███████║███████║██║     █████╔╝ ██║  ██║█████╗     ██║   █████╗  ██║        ██║   
    ██╔══██║██╔══██║██║     ██╔═██╗ ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   
    ██║  ██║██║  ██║╚██████╗██║  ██╗██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   
        """ + Style.RESET_ALL

        self.external_hacker_types = [
            "Government Agency",
            "Rival Corporation",
            "Hacktivist Group",
            "Criminal Syndicate"
        ]

    def show_tutorial(self):
        """Display game tutorial and information"""
        self.clear_screen()
        print(self.logo)
        
        tutorial_options = [
            "Game Overview",
            "How to Win",
            "Player Actions Guide",
            "Hacker Actions Guide",
            "Understanding Clues",
            "Return to Game"
        ]
        
        choice = self.ui.create_menu("TUTORIAL & HELP", tutorial_options)
        
        if choice == 1:  # Game Overview
            self.print_frame("GAME OVERVIEW")
            self.ui.print_alert_box("Welcome to HackDetect!", "info")
            self.ui.print_alert_box("A security breach has been detected in the system.", "warning")
            self.ui.print_alert_box("One player might be a hacker... or it could be an external threat.", "warning")
            self.ui.print_alert_box("Work together to find the source before it's too late!", "info")
            
        elif choice == 2:  # How to Win
            self.print_frame("HOW TO WIN")
            self.ui.print_alert_box("For Regular Agents:", "info")
            self.ui.print_alert_box("- Correctly identify the hacker or external threat", "info")
            self.ui.print_alert_box("- Submit a breach analysis report when you're confident", "info")
            self.ui.print_alert_box("For the Hacker:", "warning")
            self.ui.print_alert_box("- Remain undetected for 10 rounds", "warning")
            self.ui.print_alert_box("- Or mislead others to make wrong accusations", "warning")
            
        elif choice == 3:  # Player Actions Guide
            self.print_frame("PLAYER ACTIONS GUIDE")
            self.ui.print_alert_box("Available Actions:", "info")
            self.ui.print_alert_box("1. Scan for Security Breaches:", "info")
            self.ui.print_alert_box("   - Search the system for suspicious activity", "info")
            self.ui.print_alert_box("2. Submit Breach Analysis Report:", "info")
            self.ui.print_alert_box("   - Make an accusation when you think you found the hacker", "info")
            self.ui.print_alert_box("3. Share Intelligence:", "info")
            self.ui.print_alert_box("   - Share clues with other players", "info")
            self.ui.print_alert_box("   - Combine analysis to gain special insights", "info")
            
        elif choice == 4:  # Hacker Actions Guide
            self.print_frame("HACKER ACTIONS GUIDE")
            self.ui.print_alert_box("If you're the hacker, you can:", "warning")
            self.ui.print_alert_box("1. Plant False Evidence:", "info")
            self.ui.print_alert_box("   - Create misleading clues about other players", "info")
            self.ui.print_alert_box("2. Corrupt System Logs:", "info")
            self.ui.print_alert_box("   - Make collected evidence unreadable", "info")
            self.ui.print_alert_box("3. Deploy Counter-Surveillance:", "info")
            self.ui.print_alert_box("   - Use various tools to avoid detection", "info")
            self.ui.print_alert_box("4. Intercept Communications:", "info")
            self.ui.print_alert_box("   - See what other players are sharing", "info")
            
        elif choice == 5:  # Understanding Clues
            self.print_frame("UNDERSTANDING CLUES")
            self.ui.print_alert_box("Types of Clues:", "info")
            self.ui.print_alert_box("1. Regular System Logs:", "info")
            self.ui.print_alert_box("   - Show suspicious activity in different locations", "info")
            self.ui.print_alert_box("2. Combined Analysis:", "info")
            self.ui.print_alert_box("   - Special insights from sharing intelligence", "info")
            self.ui.print_alert_box("3. Corrupted Logs:", "warning")
            self.ui.print_alert_box("   - Damaged evidence that's hard to read", "warning")
            self.ui.print_alert_box("4. False Evidence:", "error")
            self.ui.print_alert_box("   - Misleading clues planted by the hacker", "error")
            
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)


    def print_centered(self, text: str, padding_char="═"):
        width = self.terminal_width - 4
        padded_text = text.center(width, padding_char)
        print(Fore.CYAN + f"║ {padded_text} ║" + Style.RESET_ALL)

    def print_frame(self, title: str = "", style="double"):
        width = self.terminal_width - 2
        if style == "double":
            print(Fore.CYAN + f"╔{'═' * width}╗" + Style.RESET_ALL)
            if title:
                self.print_centered(title)
                print(Fore.CYAN + f"╠{'═' * width}╣" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"┌{'─' * width}┐" + Style.RESET_ALL)

    def print_footer(self, style="double"):
        width = self.terminal_width - 2
        if style == "double":
            print(Fore.CYAN + f"╚{'═' * width}╝" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"└{'─' * width}┘" + Style.RESET_ALL)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def initialize_game(self):
        self.clear_screen()
        print(self.logo)
        self.ui.matrix_rain(1.0)
        
        self.print_frame("SYSTEM INITIALIZATION")
        self.ui.print_glitch_effect("Establishing secure connection...")
        time.sleep(0.5)
        self.ui.print_alert_box("Connection established.", "success")
        
        self.print_frame("Agent Registration")
        for i in range(self.num_players):
            player_name = input(Fore.GREEN + f"Enter codename for Agent {i+1}: " + Style.RESET_ALL).strip()
            self.players.append(Player(name=player_name))
            self.ui.print_glitch_effect(f"Agent {player_name} registered...")
            
        if self.include_external_hacker and random.random() < 0.45:
            self.external_hacker = random.choice(self.external_hacker_types)
            self.hacker_is_external = True
        else:
            hacker = random.choice(self.players)
            hacker.is_hacker = True
            self.hacker_is_external = False
        
        self.ui.print_alert_box("System breach detected...", "warning")
        self.ui.matrix_rain(1.0)

    def generate_clue(self, player: Player) -> str:
        self.print_frame("ACCESSING SYSTEM")
        self.ui.matrix_rain(0.5)
        
        # First check if player is blocked from investigating
        if not player.can_investigate:
            self.ui.print_glitch_effect("Access denied - Security protocols active...")
            return "ERROR: System access restricted - Unable to retrieve logs"
        
        # Check for planted evidence first (30% chance if available)
        if self.planted_evidence and random.random() < 0.3:
            self.ui.print_glitch_effect("Analyzing system logs...")
            planted_clue = random.choice(self.planted_evidence)
            player.clues_found.append(planted_clue)
            return planted_clue
        
        # Check for honeypot data
        if player.honeypot_data:
            clue = player.honeypot_data
            player.honeypot_data = None  # Clear the honeypot after use
            player.clues_found.append(clue)
            return clue
        
        # Generate clues specific to this player
        if self.hacker_is_external:
            clues = self.clue_system.generate_clues_for_player("EXTERNAL", player.name)
        else:
            hacker = next(p for p in self.players if p.is_hacker)
            clues = self.clue_system.generate_clues_for_player(hacker.name, player.name)
        
        # Find clues the player hasn't seen yet
        unseen_clues = [c for c in clues if c not in player.clues_found]
        
        if unseen_clues:  # If there are unseen clues, pick one
            clue = random.choice(unseen_clues)
        else:  # If all clues have been seen, generate new ones
            if self.hacker_is_external:
                clues = self.clue_system.generate_clues_for_player("EXTERNAL", player.name + str(random.random()))
            else:
                hacker = next(p for p in self.players if p.is_hacker)
                clues = self.clue_system.generate_clues_for_player(hacker.name, player.name + str(random.random()))
            clue = random.choice(clues)
        
        # Check if the selected clue has been corrupted
        if clue in player.corrupted_clues:
            self.ui.print_glitch_effect("Warning: File corruption detected...")
            corrupted_chars = '!@#$%^&*()'
            corrupted_text = ''.join(
                random.choice(corrupted_chars) if random.random() < 0.3 else c
                for c in clue
            )
            player.clues_found.append(f"CORRUPTED LOG: {corrupted_text}")
            return f"CORRUPTED LOG: {corrupted_text}"
        
        self.ui.print_glitch_effect("Decrypting data...")
        player.clues_found.append(clue)
        return clue

    def hacker_menu(self, player: Player):
        self.print_frame("SYSTEM BACKDOOR ACTIVE")
        self.ui.print_glitch_effect("Accessing root privileges...")
        
        action_taken = False
        
        while True:
            if not action_taken:
                options = [
                    "Plant false evidence",
                    "Corrupt system logs",
                    "Deploy counter-surveillance",
                    "Intercept communications",
                    "Review hacker actions",
                    "End turn"
                ]
            else:
                options = [
                    "Review hacker actions",
                    "End turn"
                ]
            
            choice = self.ui.create_menu("Select hacker action:", options)
            
            if not action_taken:
                if choice == 1:  # Plant false evidence
                    self.plant_false_evidence(player)
                    action_taken = True
                elif choice == 2:  # Corrupt system logs
                    self.corrupt_system_logs(player)
                    action_taken = True
                elif choice == 3:  # Deploy counter-surveillance
                    self.deploy_counter_surveillance(player)
                    action_taken = True
                elif choice == 4:  # Intercept communications
                    self.intercept_communications(player)
                    action_taken = True
                elif choice == 5:  # Review actions
                    self.review_hacker_actions(player)
                elif choice == 6:  # End turn
                    break
            else:
                if choice == 1:  # Review actions
                    self.review_hacker_actions(player)
                elif choice == 2:  # End turn
                    break
            
            self.clear_screen()
            print(self.logo)
            self.display_player_stats(player)
            
            if action_taken:
                self.ui.print_alert_box("NOTICE: Attack already deployed this round", "warning")

    def intercept_communications(self, hacker: Player):
        """Allows hacker to see communications between other players"""
        self.print_frame("INTERCEPTING COMMUNICATIONS")
        self.ui.matrix_rain(0.5)
        
        # Get list of potential targets (non-hacker players)
        targets = [p for p in self.players if not p.is_hacker]
        
        if not targets:
            self.ui.print_alert_box("No valid targets found", "warning")
            return
            
        # Let hacker choose a target
        options = [f"Monitor Agent {p.name}'s communications" for p in targets]
        choice = self.ui.create_menu("Select target to monitor:", options)
        target = targets[choice - 1]
        
        # Check if target has shared any intelligence
        has_shared = False
        shared_info = []
        
        for clue in target.clues_found:
            if clue.startswith("ANALYSIS:"):  # This indicates shared/combined analysis
                has_shared = True
                shared_info.append(clue)
        
        if has_shared:
            self.ui.print_alert_box(f"Intercepted communications from Agent {target.name}:", "success")
            for info in shared_info:
                self.ui.print_alert_box(info, "info")
            
            # Add intercepted info to hacker's clues
            for info in shared_info:
                if info not in hacker.clues_found:
                    hacker.clues_found.append(f"INTERCEPTED: {info}")
        else:
            self.ui.print_alert_box(f"No shared communications found for Agent {target.name}", "warning")
        
        # Set up ongoing monitoring
        hacker.active_programs[f"Monitoring_{target.name}"] = 2  # Monitor for 2 rounds
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    def plant_false_evidence(self, hacker: Player):
        """Plant misleading clues that point to other players"""
        self.print_frame("PLANTING FALSE EVIDENCE")
        self.ui.matrix_rain(0.5)
        
        # Get list of non-hacker players
        targets = [p for p in self.players if not p.is_hacker]
        
        # Let hacker choose a target to frame
        options = [f"Frame Agent {p.name}" for p in targets]
        choice = self.ui.create_menu("Select target to frame:", options)
        target = targets[choice - 1]
        
        # Generate false clue pointing to target using new system
        false_clues = self.clue_system.generate_clues_for_player(target.name, "planted_evidence_" + str(random.random()))
        false_clue = random.choice([clue for clue in false_clues if target.name in clue])  # Ensure the clue mentions the target
        
        # Add to pool of possible clues
        self.planted_evidence.append(false_clue)
        self.ui.print_alert_box("False evidence planted successfully", "success")
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        
    def corrupt_system_logs(self, hacker: Player):
        """Corrupt another player's collected evidence"""
        self.print_frame("CORRUPTING SYSTEM LOGS")
        self.ui.matrix_rain(0.5)
        
        # Get players with evidence
        targets = [p for p in self.players if p.clues_found and not p.is_hacker]
        if not targets:
            self.ui.print_alert_box("No valid targets found", "warning")
            return
                
        options = [f"Corrupt Agent {p.name}'s logs" for p in targets]
        choice = self.ui.create_menu("Select logs to corrupt:", options)
        target = targets[choice - 1]
        
        # Corrupt multiple clues (2-3 random clues)
        if target.clues_found:
            num_clues_to_corrupt = min(len(target.clues_found), random.randint(2, 3))
            clues_to_corrupt = random.sample(target.clues_found, num_clues_to_corrupt)
            for clue in clues_to_corrupt:
                target.corrupted_clues.append(clue)
            self.ui.print_alert_box(f"System logs corrupted: {num_clues_to_corrupt} files affected", "success")
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
    def display_clue(self, clue: str, player: Player) -> str:
        """Helper function to properly display clues, handling corruption"""
        if clue in player.corrupted_clues:
            corrupted_chars = '!@#$%^&*()'
            return ''.join(
                random.choice(corrupted_chars) if random.random() < 0.3 else c
                for c in clue
            )
        return clue
            
    def deploy_counter_surveillance(self, hacker: Player):
        """Simplified counter-surveillance system"""
        self.print_frame("DEPLOYING COUNTER-SURVEILLANCE")
        self.ui.matrix_rain(0.5)
        
        measures = [
            "Network Honeypot (Feeds false data to next investigator)",
            "Access Log Manipulation (Prevents investigation for 2 rounds)",
            "System Lockdown (Blocks sharing between two chosen players)",
            "Ghost Protocol (Makes your actions invisible for next round)"
        ]
        
        choice = self.ui.create_menu("Select counter-surveillance measure:", measures)
        
        if choice == 1:  # Network Honeypot
            # Create false data that will be fed to the next investigator
            honeypot_location = random.choice(self.clue_system.locations)
            false_clue = f"Suspicious activity detected in {honeypot_location} - possible security breach"
            
            # Find next player
            current_index = self.players.index(hacker)
            next_player = self.players[(current_index + 1) % len(self.players)]
            
            # Set up the honeypot
            next_player.honeypot_data = false_clue
            next_player.honeypot_expires_in = 1  # Expires after one round
            
            self.ui.print_alert_box(f"Honeypot deployed - will feed false data to Agent {next_player.name}", "success")
            
        elif choice == 2:  # Access Log Manipulation
            # Get list of potential targets
            targets = [p for p in self.players if not p.is_hacker]
            target_idx = self.ui.create_menu(
                "Select agent to block:",
                [f"Agent {p.name}" for p in targets]
            ) - 1
            target = targets[target_idx]
            
            # Set the block duration and status
            target.blocked_rounds_remaining = 2  # Will last for 2 rounds
            target.can_investigate = False  # Immediately disable investigation
            
            self.ui.print_alert_box(f"Access blocked for Agent {target.name} for {target.blocked_rounds_remaining} rounds", "success")
            self.ui.print_glitch_effect("Deploying access restrictions...")
            
        elif choice == 3:  # System Lockdown
            # Select two players to block from sharing
            targets = [p for p in self.players if not p.is_hacker]
            if len(targets) < 2:
                self.ui.print_alert_box("Not enough players to block sharing", "error")
                return
                
            print("\nSelect first agent:")
            target1_idx = self.ui.create_menu(
                "First agent:",
                [f"Agent {p.name}" for p in targets]
            ) - 1
            target1 = targets[target1_idx]
            
            # Remove first target from options
            remaining_targets = [p for p in targets if p != target1]
            
            print("\nSelect second agent:")
            target2_idx = self.ui.create_menu(
                "Second agent:",
                [f"Agent {p.name}" for p in remaining_targets]
            ) - 1
            target2 = remaining_targets[target2_idx]
            
            # Block sharing between these players
            blocked_pair = frozenset([target1.name, target2.name])
            self.blocked_sharing.add(blocked_pair)
            
            self.ui.print_alert_box(f"Communication blocked between Agent {target1.name} and Agent {target2.name}", "success")
            
        elif choice == 4:  # Ghost Protocol
            hacker.ghost_mode = True
            hacker.active_programs["Ghost_Protocol"] = 1
            
            self.ui.print_alert_box("Ghost Protocol activated - your actions will be invisible next round", "success")
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    def review_hacker_actions(self, hacker: Player):
        """Review all hacker actions taken"""
        self.print_frame("REVIEWING PLANTED EVIDENCE")
        
        if self.planted_evidence:
            for i, evidence in enumerate(self.planted_evidence, 1):
                self.ui.print_alert_box(f"{i}. {evidence}", "info")
        else:
            self.ui.print_alert_box("No false evidence planted", "info")
            
        if any(p.corrupted_clues for p in self.players):
            self.print_frame("CORRUPTED LOGS")
            for player in self.players:
                if player.corrupted_clues:
                    for clue in player.corrupted_clues:
                        self.ui.print_alert_box(f"Agent {player.name}: {clue}", "info")
                        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    def regular_player_turn(self, player: Player):
        self.display_player_stats(player)
        action_taken = False
        
        while True:
            print(f"\n{Fore.CYAN}AVAILABLE ACTIONS{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{'═' * len('AVAILABLE ACTIONS')}{Style.RESET_ALL}")
            
            if not action_taken:
                options = [
                    "Scan for security breaches",
                    "Submit breach analysis report",
                    "Review collected data",
                    "Share intelligence",
                    "Access Tutorial",
                    "End investigation phase"
                ]
                
                for i, option in enumerate(options, 1):
                    if not player.can_investigate and option == "Scan for security breaches":
                        print(f"{Style.DIM}{Fore.RED}{i}. {option} (BLOCKED - {player.blocked_rounds_remaining} rounds remaining){Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}{i}{Style.RESET_ALL}. {option}")
            else:
                options = ["Review collected data", "End investigation phase"]
                for i, option in enumerate(options, 1):
                    print(f"{Fore.YELLOW}{i}{Style.RESET_ALL}. {option}")
                self.ui.print_alert_box("NOTICE: Investigation action completed for this round", "info")
        
            try:
                choice = int(input(f"\n{Fore.GREEN}Enter your choice >{Style.RESET_ALL} "))
                
                if not action_taken:
                    if 1 <= choice <= len(options):
                        selected_option = options[choice - 1]
                        
                        if selected_option == "Scan for security breaches":
                            if not player.can_investigate:
                                self.ui.print_alert_box("ERROR: Security systems are blocking access", "error")
                                continue
                            self.print_frame("SCANNING SYSTEM")
                            self.ui.matrix_rain(0.5)
                            clue = self.generate_clue(player)
                            self.ui.print_alert_box(clue, "info")
                            action_taken = True
                            
                        elif selected_option == "Submit breach analysis report":
                            self.make_accusation(player)
                            if self.game_over:
                                return
                            action_taken = True
                            
                        elif selected_option == "Review collected data":
                            self.print_frame("COLLECTED DATA")
                            if player.clues_found:
                                for i, clue in enumerate(player.clues_found, 1):
                                    displayed_clue = self.display_clue(clue, player)
                                    if clue in player.corrupted_clues:
                                        self.ui.print_alert_box(f"{i}. CORRUPTED LOG: {displayed_clue}", "error")
                                    else:
                                        self.ui.print_alert_box(f"{i}. {displayed_clue}", "info")
                            else:
                                self.ui.print_alert_box("No data collected yet", "warning")
                                
                        elif selected_option == "Share intelligence":
                            self.share_intelligence(player)
                            action_taken = True

                        elif selected_option == "Access Tutorial":
                            self.show_tutorial()
                            
                        elif selected_option == "End investigation phase":
                            break

                else:  # After action taken
                    if 1 <= choice <= len(options):
                        selected_option = options[choice - 1]
                        
                        if selected_option == "Review collected data":
                            self.print_frame("COLLECTED DATA")
                            if player.clues_found:
                                for i, clue in enumerate(player.clues_found, 1):
                                    displayed_clue = self.display_clue(clue, player)
                                    if clue in player.corrupted_clues:
                                        self.ui.print_alert_box(f"{i}. CORRUPTED LOG: {displayed_clue}", "error")
                                    else:
                                        self.ui.print_alert_box(f"{i}. {displayed_clue}", "info")
                            else:
                                self.ui.print_alert_box("No data collected yet", "warning")
                        elif selected_option == "End investigation phase":
                            break
                            
                input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
                
            except ValueError:
                self.ui.print_alert_box("Please enter a number", "error")
            
            self.clear_screen()
            print(self.logo)
            self.ui.matrix_rain(0.5)
            self.display_player_stats(player)
            
    def share_intelligence(self, player: Player):
        """Allow players to share clues or combine analysis"""
        # Get list of other players
        other_players = [p for p in self.players if p != player]
        if not other_players:
            self.ui.print_alert_box("No other players to share with", "error")
            return
                
        # Select player to share with
        target_idx = self.ui.create_menu(
            "Share intelligence with:",
            [p.name for p in other_players]
        ) - 1
        target_player = other_players[target_idx]
        
        # Check if sharing is blocked between these players
        if frozenset([player.name, target_player.name]) in self.blocked_sharing:
            self.ui.print_alert_box("ERROR: Communication blocked between agents", "error")
            return
        
        share_options = [
            "Share clue",
            "Combine analysis"
        ]
        
        action = self.ui.create_menu("Select sharing action:", share_options)
        
        if action == 1:  # Share clue
            if not player.clues_found:
                self.ui.print_alert_box("No clues available to share", "warning")
                return
                
            # Let player select which clue to share
            uncorrupted_clues = [clue for clue in player.clues_found if clue not in player.corrupted_clues]
            if not uncorrupted_clues:
                self.ui.print_alert_box("All your clues are corrupted!", "error")
                return

            options = [f"Clue {i+1}: {clue}" for i, clue in enumerate(uncorrupted_clues)]
            clue_idx = self.ui.create_menu("Select clue to share:", options) - 1
            shared_clue = uncorrupted_clues[clue_idx]
            
            # Add clue to target player's collection
            if shared_clue not in target_player.clues_found:
                target_player.clues_found.append(shared_clue)
                self.ui.print_alert_box(f"Clue shared with Agent {target_player.name}", "success")
            else:
                self.ui.print_alert_box("Agent already has this information", "warning")
                    
        elif action == 2:  # Combine analysis
            # Players can combine their clues to get a special insight
            if not player.clues_found or not target_player.clues_found:
                self.ui.print_alert_box("Both agents need clues to combine analysis", "error")
                return
                    
            # Find common elements between clues
            player_locations = set()
            target_locations = set()
            
            # Extract locations from clues
            for clue in player.clues_found:
                if clue in player.corrupted_clues:
                    continue  # Skip corrupted clues
                for location in self.clue_system.locations:
                    if location in clue:
                        player_locations.add(location)
                        
            for clue in target_player.clues_found:
                if clue in target_player.corrupted_clues:
                    continue  # Skip corrupted clues
                for location in self.clue_system.locations:
                    if location in clue:
                        target_locations.add(location)
            
            # Find overlapping locations
            common_locations = player_locations.intersection(target_locations)
            
            if common_locations:
                # Generate a special insight based on common locations
                location = random.choice(list(common_locations))
                if self.hacker_is_external:
                    insight = f"Combined analysis reveals concentrated activity in {location}"
                else:
                    hacker = next(p for p in self.players if p.is_hacker)
                    if random.random() < 0.3:  # 30% chance to get valuable insight
                        insight = f"Pattern analysis shows Agent {hacker.name} accessed {location} multiple times"
                    else:
                        insight = f"Multiple security anomalies detected in {location}"
                
                # Add insight to both players' clues
                combined_insight = f"ANALYSIS: {insight}"
                player.clues_found.append(combined_insight)
                target_player.clues_found.append(combined_insight)
                
                self.ui.print_alert_box("Combined analysis complete - new insights added", "success")
            else:
                self.ui.print_alert_box("No correlation found in combined analysis", "warning")
            
            input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        
    def play_round(self):
        self.clear_screen()
        print(self.logo)
        self.ui.matrix_rain(0.5)
        
        self.print_frame(f"ROUND {self.current_round}")
        progress = self.current_round / self.max_rounds
        print("\n" + self.ui.create_progress_bar(progress))
        self.print_footer()
        
        for player in self.players:
            input(Fore.YELLOW + f"\nPress Enter for Agent {player.name}'s turn (other agents avert your eyes)" + Style.RESET_ALL)
            self.clear_screen()
            print(self.logo)
            self.ui.matrix_rain(0.5)  # Add matrix effect for every player transition
            
            if player.is_hacker:
                self.ui.print_glitch_effect("ROOT ACCESS DETECTED")
                self.ui.print_alert_box("ADMINISTRATOR PRIVILEGES GRANTED", "warning")
                self.hacker_menu(player)
            else:
                # Add a transition effect when switching from hacker to regular player
                if any(p.is_hacker for p in self.players if p != player):
                    self.ui.print_glitch_effect("Secure connection established...")
                    self.ui.print_alert_box("Standard user access granted", "info")
                self.regular_player_turn(player)

            # Add matrix effect after each player's turn
            if player != self.players[-1]:  # If not the last player
                self.clear_screen()
                print(self.logo)
                self.ui.matrix_rain(0.5)

        self.update_player_states()
        
        self.current_round += 1
        if self.current_round > self.max_rounds:
            self.game_over = True
            self.hacker_won = True

    def update_player_states(self):
        """Update player states at the end of each round"""
        for player in self.players:
            # Update blocked investigation duration
            if player.blocked_rounds_remaining > 0:
                player.blocked_rounds_remaining -= 1
                if player.blocked_rounds_remaining == 0:
                    player.can_investigate = True
                    self.ui.print_alert_box(f"Agent {player.name}'s access has been restored", "info")
                else:
                    self.ui.print_alert_box(f"Agent {player.name}'s access will remain blocked for {player.blocked_rounds_remaining} more rounds", "warning")

            # Clear expired honeypots
            if player.honeypot_data and player.honeypot_expires_in > 0:
                player.honeypot_expires_in -= 1
                if player.honeypot_expires_in == 0:
                    player.honeypot_data = None
            
            # Reset ghost mode
            if player.ghost_mode:
                player.ghost_mode = False
            
            # Update forced investigation
            if player.forced_investigation:
                player.forced_investigation = None


    def make_accusation(self, accuser: Player):
        self.print_frame("SUBMIT BREACH ANALYSIS")
        
        options = []
        if self.include_external_hacker:
            options.append("External Security Breach")
        
        # Add all players except the accuser to the options
        for player in self.players:
            if player != accuser:
                options.append(f"Agent {player.name}")
                
        self.ui.print_glitch_effect("Analyzing collected data...")
        
        choice = self.ui.create_menu("Select suspected source of breach:", options)
        
        self.print_frame("ANALYSIS RESULTS")
        
        # If external hacker is enabled and they chose it (first option)
        if self.include_external_hacker and choice == 1:
            if self.hacker_is_external:
                self.game_over = True
                self.hacker_won = False
                self.ui.print_alert_box("CONFIRMATION: External breach detected and contained!", "success")
                input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
                return True  # Return True to indicate game should end
            else:
                self.ui.print_alert_box("ERROR: Analysis inconclusive - Check collected data", "error")
        else:
            # Adjust the index based on whether external hacker is included
            player_index = choice - 1 - (1 if self.include_external_hacker else 0)
            
            # Find the accused player
            accused = None
            players_excluding_accuser = [p for p in self.players if p != accuser]
            if 0 <= player_index < len(players_excluding_accuser):
                accused = players_excluding_accuser[player_index]
                    
            if accused and accused.is_hacker:
                self.game_over = True
                self.hacker_won = False
                self.ui.print_alert_box(f"CONFIRMATION: Internal breach source identified - Agent {accused.name}", "success")
                input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
                return True  # Return True to indicate game should end
            else:
                if accused:
                    self.ui.print_alert_box(f"ERROR: Analysis inconclusive - Agent {accused.name} is not the source", "error")
                else:
                    self.ui.print_alert_box("ERROR: Analysis inconclusive - Check collected data", "error")
                
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return False  # Return False to continue the game

    def display_player_stats(self, player: Player):
        self.print_frame(f"Agent: {player.name}")
        progress = len(player.clues_found) / 10
        print("\n" + self.ui.create_progress_bar(progress))
        self.print_centered(f"Round: {self.current_round}/{self.max_rounds}")
        self.print_centered(f"Clues Discovered: {len(player.clues_found)}")
        if player.is_hacker:
            self.print_centered(f"Role: SYSTEM ADMINISTRATOR")
            self.print_centered(f"False Evidence Planted: {len(self.planted_evidence)}")
        self.print_footer()

    def run_game(self):
        self.initialize_game()
        
        while not self.game_over:
            self.play_round()
            
        self.clear_screen()
        print(self.logo)
        self.ui.matrix_rain(1.0)
        
        self.print_frame("Mission Report")
        if self.hacker_won:
            self.ui.print_alert_box("MISSION FAILED: The breach remains active...", "error")
            if self.hacker_is_external:
                hacker_type = self.external_hacker
                self.ui.print_alert_box(f"The {hacker_type} has successfully infiltrated our systems.", "error")
            else:
                hacker = next(p for p in self.players if p.is_hacker)
                self.ui.print_alert_box(f"Agent {hacker.name} has successfully compromised our security.", "error")
        else:
            self.ui.print_alert_box("MISSION SUCCESSFUL: Threat neutralized!", "success")
        self.print_footer()

def main():
    try:
        import logging
        logging.basicConfig(filename='hackdetect.log', level=logging.DEBUG)
        
        try:
            width = os.get_terminal_size().columns
            if width < 90:
                print(Fore.RED + "Please resize terminal to at least 90 columns wide. Press Enter to exit..." + Style.RESET_ALL)
                input()
                return
        except:
            logging.warning("Could not determine terminal size")
            pass

        def show_main_menu():
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen before showing menu
            
            title = Fore.CYAN + """
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██████╗ ███████╗████████╗███████╗ ██████╗████████╗
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
    ███████║███████║██║     █████╔╝ ██║  ██║█████╗     ██║   █████╗  ██║        ██║   
    ██╔══██║██╔══██║██║     ██╔═██╗ ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   
    ██║  ██║██║  ██║╚██████╗██║  ██╗██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   
""" + Fore.RED + """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                        BREACH PROTOCOL: CLASSIFIED                           ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
""" + Fore.YELLOW + """
                              Trust No One...
                        Not Even Your Terminal
""" + Style.BRIGHT + Fore.CYAN + """
    ╔══════════════════════════════════════════════════════════════════════════════════════════╗""" + \
    Fore.RED + """
    ║                WARNING: SECURITY BREACH DETECTED - INITIATING CONTAINMENT PROTOCOLS      ║""" + \
    Fore.CYAN + """
    ╚══════════════════════════════════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL

            # Calculate space needed for options to keep input at bottom
            menu_height = 20  # Approximate height of menu including title
            current_height = len(title.split('\n'))
            padding = menu_height - current_height
            
            print(title + "\n" * padding)
            
            # Create UI instance for menu
            ui = EnhancedUI()
            
            # Matrix rain effect for atmosphere (shorter duration)
            ui.matrix_rain(0.5)
            
            # Add tutorial option at start
            start_options = [
                "INITIATE NEW INVESTIGATION",
                "ACCESS TRAINING PROTOCOLS (Tutorial)",
                "TERMINATE SESSION"
            ]
            
            return ui.create_menu("MAIN INTERFACE", start_options)

        while True:
            choice = show_main_menu()
            
            if choice == 1:  # Start New Game
                while True:
                    try:
                        num_players = int(input(Fore.GREEN + "Number of agents to deploy (2-8): " + Style.RESET_ALL))
                        if 2 <= num_players <= 8:
                            break
                        print(Fore.RED + "Please enter a number between 2 and 8" + Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED + "Please enter a valid number" + Style.RESET_ALL)
                
                include_external = input(Fore.GREEN + "Enable external threat monitoring? (y/n): " + Style.RESET_ALL).lower() == 'y'
                
                game = HackerGame(num_players, include_external)
                game.run_game()
                break  # Exit after game ends
                
            elif choice == 2:  # Tutorial
                game = HackerGame(2, True)  # Create temporary game instance for tutorial
                game.show_tutorial()
                continue  # Return to main menu after tutorial
                
            elif choice == 3:  # Exit
                ui = EnhancedUI()
                ui.print_glitch_effect("Terminating secure connection...")
                print("\nConnection terminated. Thank you for your service.")
                return
        
    except Exception as e:
        # Log the error
        logging.error(f"An error occurred: {str(e)}", exc_info=True)
        print(Fore.RED + f"An error occurred: {str(e)}" + Style.RESET_ALL)
    
    finally:
        print("\nPress Enter to exit...")
        input()

if __name__ == "__main__":
    main()
    