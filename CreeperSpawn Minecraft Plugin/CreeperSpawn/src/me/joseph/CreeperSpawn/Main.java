package me.joseph.CreeperSpawn;

import org.bukkit.plugin.java.JavaPlugin;

import me.joseph.CreeperSpawn.commands.CreeperCommand;

public class Main extends JavaPlugin{
	
	@Override
	public void onEnable() {
		new CreeperCommand(this);
	}
}
