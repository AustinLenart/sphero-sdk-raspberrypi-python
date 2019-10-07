import asyncio
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrAsync
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import SerialAsyncDal


loop = asyncio.get_event_loop()

rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)


async def main():
    """ This program demonstrates how to set a single LED on RVR using the LED control helper.
    """

    await rvr.wake()

    # give RVR time to wake up
    await asyncio.sleep(2)

    await rvr.led_control.turn_leds_off()

    # delay to show LEDs change
    await asyncio.sleep(1)

    await rvr.led_control.set_led_rgb(
        led=RvrLedGroups.headlight_right,
        red=255,
        green=0,
        blue=0
    )

    # delay to show LEDs change
    await asyncio.sleep(1)

    await rvr.led_control.set_led_color(
        led=RvrLedGroups.headlight_left,
        color=Colors.green
    )

    # delay to show LEDs change
    await asyncio.sleep(1)

    await rvr.close()


if __name__ == '__main__':
    try:
        loop.run_until_complete(
            main()
        )

    except KeyboardInterrupt:
        print('Program terminated with keyboard interrupt.')

    finally:
        loop.run_until_complete(
            rvr.close()
        )

        if loop.is_running():
            loop.close()
