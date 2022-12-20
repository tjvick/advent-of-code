from enum import Enum

from solutions import helpers
import numpy as np
import re
from dataclasses import dataclass, replace

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

n_minutes = 24

strings = helpers.read_each_line_as_string(filename)


class BuildOption(Enum):
    NOTHING = 0
    OREBOT = 1
    CLAYBOT = 2
    OBSIBOT = 3
    GEOBOT = 4


@dataclass
class Supply:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geodes: int = 0
    orebot: int = 0
    claybot: int = 0
    obsibot: int = 0
    geobot: int = 0
    time: int = 0


@dataclass
class Blueprint:
    blueprint_id: int
    orebot_cost_ore: int
    claybot_cost_ore: int
    obsibot_cost_ore: int
    obsibot_cost_clay: int
    geobot_cost_ore: int
    geobot_cost_obsidian: int

    def determine_eligible_builds(self, supply):
        eligible_builds = []
        if supply.ore >= self.geobot_cost_ore and supply.obsidian >= self.geobot_cost_obsidian:
            eligible_builds.append(BuildOption.GEOBOT)
        if supply.ore >= self.obsibot_cost_ore and supply.clay >= self.obsibot_cost_clay:
            # if (supply.obsidian + supply.obsibot * supply.time) <= (self.geobot_cost_obsidian * (supply.time-1)):
            eligible_builds.append(BuildOption.OBSIBOT)
        if supply.ore >= self.claybot_cost_ore:
            # if (supply.clay + supply.claybot * supply.time) <= (self.obsibot_cost_clay * (supply.time-2)):
            eligible_builds.append(BuildOption.CLAYBOT)
        if supply.ore >= self.orebot_cost_ore:
            # if (supply.ore + supply.orebot * supply.time) <= max(self.claybot_cost_ore * (supply.time - 3), self.obsibot_cost_ore * (supply.time - 2), self.geobot_cost_ore * (supply.time - 1)):
            eligible_builds.append(BuildOption.OREBOT)

        eligible_builds.append(BuildOption.NOTHING)

        return eligible_builds

    def determine_potential_next_builds(self, supply):
        potential_next_builds = []
        if self.will_have_enough_ore_to_build(supply, self.orebot_cost_ore, dt=-2):
            potential_next_builds.append(BuildOption.OREBOT)
        if self.will_have_enough_ore_to_build(supply, self.claybot_cost_ore, dt=-2):
            potential_next_builds.append(BuildOption.CLAYBOT)
        if self.will_have_enough_clay_to_build(supply, self.obsibot_cost_clay, dt=-2) and self.will_have_enough_ore_to_build(supply, self.obsibot_cost_ore, dt=-2):
            potential_next_builds.append(BuildOption.OBSIBOT)
        if self.will_have_enough_ore_to_build(supply, self.geobot_cost_ore, dt=-1) and self.will_have_enough_obsidian_to_build(supply, self.geobot_cost_obsidian, dt=-1):
            potential_next_builds.append(BuildOption.GEOBOT)
        return potential_next_builds

    def will_have_enough_obsidian_to_build(self, supply: Supply, cost, dt=0):
        return supply.obsidian + (supply.obsibot * (supply.time+dt)) >= cost

    def will_have_enough_clay_to_build(self, supply: Supply, cost, dt=0):
        return supply.clay + (supply.claybot * (supply.time+dt)) >= cost

    def will_have_enough_ore_to_build(self, supply: Supply, cost, dt=0):
        return supply.ore + (supply.orebot * (supply.time+dt)) >= cost

    def build(self, supp, build_option: BuildOption):
        supp.time += -1
        if build_option == BuildOption.OREBOT:
            supp.ore -= self.orebot_cost_ore
            supp.orebot += 1
        elif build_option == BuildOption.CLAYBOT:
            supp.ore -= self.claybot_cost_ore
            supp.claybot += 1
        elif build_option == BuildOption.OBSIBOT:
            supp.ore -= self.obsibot_cost_ore
            supp.clay -= self.obsibot_cost_clay
            supp.obsibot += 1
        elif build_option == BuildOption.GEOBOT:
            supp.ore -= self.geobot_cost_ore
            supp.obsidian -= self.geobot_cost_obsidian
            supp.geobot += 1
        return replace(supp)

    def collect(self, supp):
        supp.ore += supp.orebot
        supp.clay += supp.claybot
        supp.obsidian += supp.obsibot
        supp.geodes += supp.geobot
        return replace(supp)

    def build_next_build(self, supply, next_build):
        new_supply = replace(supply)
        while new_supply.time > 0:
            if next_build in self.determine_eligible_builds(new_supply):
                new_supply = self.collect(new_supply)
                new_supply = self.build(new_supply, next_build)
                return new_supply

            new_supply = self.collect(new_supply)
            new_supply = self.build(new_supply, BuildOption.NOTHING)


def evaluate_blueprint(blueprint: Blueprint):
    starting_supply = Supply(orebot=1, time=n_minutes)
    max_geodes = 0
    supply_paths = [starting_supply]

    def worse_than_max(supply: Supply):
        max_possible = supply.geodes + supply.time * supply.geobot + sum(range(supply.time))
        if max_possible < max_geodes:
            return True
        return False

    while len(supply_paths) > 0:
        supply = supply_paths.pop()
        # print(supply)
        if supply.geodes > max_geodes:
            max_geodes = supply.geodes
            # max_supply = replace(supply)
            print("max_geodes", max_geodes)
            print(supply)

        if supply.time > 0:
            potential_next_builds = blueprint.determine_potential_next_builds(supply)
            if len(potential_next_builds) == 0:
                new_supply = replace(supply)
                while new_supply.time > 0:
                    new_supply = blueprint.collect(new_supply)
                    new_supply = blueprint.build(new_supply, BuildOption.NOTHING)
                if not worse_than_max(new_supply):
                    supply_paths.append(new_supply)

            for potential_next_build in potential_next_builds:
                new_supply = blueprint.build_next_build(replace(supply), potential_next_build)
                if new_supply is not None and not worse_than_max(new_supply):
                    supply_paths.append(new_supply)


    return blueprint.blueprint_id * max_geodes


total_quality_level = 0

for string in strings[:]:
    m = re.match(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', string)
    (
        blueprint_id,
        orebot_cost_ore,
        claybot_cost_ore,
        obsibot_cost_ore,
        obsibot_cost_clay,
        geobot_cost_ore,
        geobot_cost_obsidian
    ) = (int(x) for x in m.groups())

    bp = Blueprint(
        blueprint_id,
        orebot_cost_ore,
        claybot_cost_ore,
        obsibot_cost_ore,
        obsibot_cost_clay,
        geobot_cost_ore,
        geobot_cost_obsidian
    )

    print("BLUEPRINT", bp.blueprint_id)
    print(bp)
    quality_level = evaluate_blueprint(bp)

    total_quality_level += quality_level

print(total_quality_level)

